from simulation.constants.electrical_types import ElectricalType
from simulation.constants.equipment_states import EquipmentStates
from simulation.models.control_room_columbia.general_physics import ac_power
from simulation.models.control_room_columbia import model
from simulation.models.control_room_columbia.general_physics import gas
import math

from enum import IntEnum

class FluidTypes(IntEnum):
    Liquid = 1,
    Gas = 2,

def clamp(val, clamp_min, clamp_max):
    return min(max(val,clamp_min),clamp_max)


headers = { #most lines have a common header that they discharge into
    #this header can pressurize and etc.
    #takes a pipe diameter and length.
    "hpcs_discharge_header" : {
        #This next comment will be present on ALL headers.
        #it indicates the real pipe that this header was made from.
        #16" HPCS(1)-4-1

        "diameter" : 406.40, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid, #Initialized on start. Is not changed again.
        "mass" : 0,
    },
    "hpcs_suction_header" : {
        #24" HPCS(2)-1-1

        "diameter" : 609.60, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },

    "lpcs_discharge_header" : {
        #6"RCIC(1)-4-1

        "diameter" : 406.40, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },
    "lpcs_suction_header" : {
        #8"RCIC(2)-1-1

        "diameter" : 609.60, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },

    "rhr_a_main_header" : {
        #18" RHR(1)-2-5

        "diameter" : 457.20, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },
    "rhr_a_discharge_header" : {
        #18" RHR(1)-2-4

        "diameter" : 457.20, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },
    "rhr_a_suction_header" : {
        #24" RHR(2)-2-2

        "diameter" : 609.60, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },

    "rhr_b_main_header" : {
        #18" RHR(1)-2-5

        "diameter" : 457.20, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },
    "rhr_b_discharge_header" : {
        #18" RHR(1)-2-4

        "diameter" : 457.20, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },
    "rhr_b_suction_header" : {
        #24" RHR(2)-2-2

        "diameter" : 609.60, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },
    #we dont have RHR C's P&ID
    "rhr_c_discharge_header" : {
        #18"

        "diameter" : 457.20, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },
    "rhr_c_suction_header" : {
        #24"

        "diameter" : 609.60, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },

    "rhr_p_3_discharge_header" : {
        #24"

        "diameter" : 609.60, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },

    #Nuclear Boiler / Main Steam System

    "main_steam_line_a_drywell" : {
        #26" MS(1)-4-2 (G.E) (LINE "B")

        "diameter" : 660.40, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "main_steam_line_a_penetration" : {
        #26" MS(1)-4-2 (G.E) (LINE "B")

        "diameter" : 660.40, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "main_steam_line_a_tunnel" : {
        #26" MS(1)-4-2 (G.E) (LINE "B")

        "diameter" : 660.40, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "main_steam_line_b_drywell" : {
        #26" MS(1)-4-2 (G.E) (LINE "B")

        "diameter" : 660.40, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "main_steam_line_b_penetration" : {
        #26" MS(1)-4-2 (G.E) (LINE "B")

        "diameter" : 660.40, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "main_steam_line_b_tunnel" : {
        #26" MS(1)-4-2 (G.E) (LINE "B")

        "diameter" : 660.40, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },

    "main_steam_line_c_drywell" : {
        #26" MS(1)-4-2 (G.E) (LINE "B")

        "diameter" : 660.40, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "main_steam_line_c_penetration" : {
        #26" MS(1)-4-2 (G.E) (LINE "B")

        "diameter" : 660.40, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "main_steam_line_c_tunnel" : {
        #26" MS(1)-4-2 (G.E) (LINE "B")

        "diameter" : 660.40, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },

    "main_steam_line_d_drywell" : {
        #26" MS(1)-4-2 (G.E) (LINE "B")

        "diameter" : 660.40, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "main_steam_line_d_penetration" : {
        #26" MS(1)-4-2 (G.E) (LINE "B")

        "diameter" : 660.40, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "main_steam_line_d_tunnel" : {
        #26" MS(1)-4-2 (G.E) (LINE "B")

        "diameter" : 660.40, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },

    #Main Steam System

    "bypass_steam_header" : {
        #24" MS (1)-4-31

        "diameter" : 609.60, #millimeters
        "length" : 20000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "turbine_bypass_manifold" : {
        #Unknown diameter. Assume 30"?

        "diameter" : 762.00, #millimeters
        "length" : 200000, #increased length due to this needing to bypass a lot of steam
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },

    "fake_turbine" : {
        #this shit fake it dont have a pipe

        "diameter" : 762.00, #millimeters
        "length" : 200000, #increased length due to this needing to bypass a lot of steam
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "rft_dt_1a_stop" : {
        #6" MS(5)-4

        "diameter" : 152.4, #millimeters
        "length" : 200000,
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "rft_dt_1b_stop" : {
        #6" MS(5)-4

        "diameter" : 152.4, #millimeters
        "length" : 200000,
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },


    "rcic_isolation_steam_line" : {
        #4"RCIC(13)-4-1

        "diameter" : 101.60, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "rcic_main_steam_line" : {
        #4"RCIC(13)-4-1

        "diameter" : 101.60, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "rcic_turbine_steam_line" : {
        #4"RCIC(13)-4-1

        "diameter" : 101.60, #millimeters
        "length" : 200000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },
    "rcic_exhaust_steam_line" : {
        #10"RCIC(16)-1-1

        "diameter" : 254, #millimeters
        "length" : 2000000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Gas,
        "mass" : 0,
    },

    "rcic_discharge_header" : {
        #6"RCIC(1)-4-1

        "diameter" : 152.40, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },
    "rcic_suction_header" : {
        #8"RCIC(2)-1-1

        "diameter" : 203.20, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },

    #Condensate
    "condensate_suction" : {
        #48"COND(1)-1

        "diameter" : 1219.20, #millimeters
        "length" : 2000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },

    "condensate_discharge" : {
        #36"COND(2)-1

        "diameter" : 914.40, #millimeters
        "length" : 6000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },

    #TODO: Condensate pumps do NOT take suction directly from condensate pumps, they pass through a few condensers first.

    #TODO: Min flow

    "condensate_booster_discharge" : {
        #30"COND(4)-3

        "diameter" : 1016, #millimeters
        "length" : 6000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },

    #TODO: RFW Pumps do NOT take suction directly from condensate booster pumps, they pass through the LP heaters first (M504-1)

    "rfw_p_1a_discharge" : {
        #24"RFW(1)-5

        "diameter" : 609.6, #millimeters
        "length" : 6000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },
    "rfw_p_1b_discharge" : {
        #24"RFW(1)-5

        "diameter" : 609.6, #millimeters
        "length" : 6000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },
    "rfw_discharge" : {
        #30"RFW(1)-4

        "diameter" : 762, #millimeters
        "length" : 8000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },

    #HX

    "rfw_hx_6a" : {
        #24"RFW(1)-4

        "diameter" : 762, #millimeters
        "length" : 10000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },
    "rfw_hx_6b" : {
        #24"RFW(1)-4

        "diameter" : 762, #millimeters
        "length" : 10000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },

    "rfw_outlet" : {
        #30"RFW(1)-4

        "diameter" : 762, #millimeters
        "length" : 10000, #TODO : determine a good length
        "pressure" : 0, #pascals
        "volume" : 0,
        "type" : FluidTypes.Liquid,
        "mass" : 0,
    },


}

from enum import IntEnum

class StaticTanks(IntEnum):
    Reactor = 1
    Wetwell = 2,
    SteamDome = 3,
    Hotwell = 4,

valves = {
    "hpcs_v_4" : { #The flow through a valve is not linear. Exponents?
        "control_switch" : "hpcs_v_4",
        "input" : "hpcs_discharge_header",
        "output" : StaticTanks.Reactor,
        "percent_open" : 0,
        "diameter" : 406.40, #mm
        "open_speed" : 0.333, #30 seconds to open from full closed.
        "seal_in" : True, #Valve is seal-in, meaning it is not throttable (normally)
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "hpcs_v_1" : {
        "control_switch" : "hpcs_v_1",
        "input" : "hpcs_discharge_header",
        "output" : StaticTanks.Reactor,
        "percent_open" : 0,
        "diameter" : 406.40, #mm
        "open_speed" : 0.333, #30 seconds to open from full closed.
        "seal_in" : True, 
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "hpcs_v_12" : { 
        "control_switch" : "hpcs_v_12",
        "input" : "hpcs_discharge_header",
        "output" : StaticTanks.Wetwell,
        "percent_open" : 100,
        "diameter" : 101.60, #mm 4 in
        "open_speed" : 0.333, #30 seconds to open from full closed.
        "seal_in" : True, 
        "sealed_in" : True, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "hpcs_v_15" : { 
        "control_switch" : "hpcs_v_15",
        "input" : StaticTanks.Wetwell,
        "output" : "hpcs_suction_header",
        "percent_open" : 100,
        "diameter" : 609.60, #mm, 24 in
        "open_speed" : 0.333, #30 seconds to open from full closed.
        "seal_in" : True, 
        "sealed_in" : True, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "hpcs_v_23" : {
        "control_switch" : "hpcs_v_23",
        "input" : "hpcs_discharge_header",
        "output" : StaticTanks.Wetwell,
        "percent_open" : 0,
        "diameter" : 406.40, #mm
        "open_speed" : 0.333, #30 seconds to open from full closed.
        "seal_in" : True,
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },

    "lpcs_v_5" : {
        "control_switch" : "lpcs_v_5",
        "input" : "lpcs_discharge_header",
        "output" : StaticTanks.Reactor,
        "percent_open" : 0,
        "diameter" : 406.40, #mm
        "open_speed" : 0.333, #30 seconds to open from full closed.
        "seal_in" : True, #Valve is seal-in, meaning it is not throttable (normally)
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "lpcs_v_11" : { 
        "control_switch" : "lpcs_v_11",
        "input" : "lpcs_discharge_header",
        "output" : StaticTanks.Wetwell,
        "percent_open" : 100,
        "diameter" : 101.60, #mm 4 in
        "open_speed" : 0.333, #30 seconds to open from full closed.
        "seal_in" : True, 
        "sealed_in" : True, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "lpcs_v_1" : { 
        "control_switch" : "lpcs_v_1",
        "input" : StaticTanks.Wetwell,
        "output" : "lpcs_suction_header",
        "percent_open" : 100,
        "diameter" : 609.60, #mm, 24 in
        "open_speed" : 0.333, #30 seconds to open from full closed.
        "seal_in" : True, 
        "sealed_in" : True, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "lpcs_v_12" : {
        "control_switch" : "lpcs_v_12",
        "input" : "lpcs_discharge_header",
        "output" : StaticTanks.Wetwell,
        "percent_open" : 0,
        "diameter" : 406.40, #mm
        "open_speed" : 0.333, #30 seconds to open from full closed.
        "seal_in" : True,
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },

    "rhr_v_4a" : { 
        "control_switch" : "rhr_v_4a",
        "input" : StaticTanks.Wetwell,
        "output" : "rhr_a_suction_header",
        "percent_open" : 100,
        "diameter" : 609.60, #mm, 24 in
        "open_speed" : 0.0666, #2.5 minutes to open from full closed.
        "seal_in" : True, 
        "sealed_in" : True, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "rhr_v_6a" : { 
        "control_switch" : "rhr_v_6a",
        "input" : StaticTanks.Reactor,
        "output" : "rhr_a_suction_header",
        "percent_open" : 0,
        "diameter" : 609.60, #mm, 24 in
        "open_speed" : 0.0666, #2.5 minutes to open from full closed.
        "seal_in" : True, 
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "rhr_v_48a" : { 
        "control_switch" : "rhr_v_48a",
        "input" : "rhr_a_discharge_header",
        "output" : "rhr_a_main_header",
        "percent_open" : 100,
        "diameter" : 457.20, #mm, 18 in
        "open_speed" : 0.0666, #2.5 minutes to open from full closed.
        "seal_in" : False, 
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "rhr_v_3a" : { 
        "control_switch" : "rhr_v_3a",
        "input" : "rhr_a_discharge_header",
        "output" : "rhr_a_main_header",
        "percent_open" : 100,
        "diameter" : 457.20, #mm, 18 in
        "open_speed" : 0.0666, #2.5 minutes to open from full closed.
        "seal_in" : False, 
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "rhr_v_42a" : { 
        "control_switch" : "rhr_v_42a",
        "input" : "rhr_a_main_header",
        "output" : StaticTanks.Reactor,
        "percent_open" : 0,
        "diameter" : 355.60, #mm, 14 in
        "open_speed" : 0.333, #30 seconds to open from full closed.
        "seal_in" : True, 
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "rhr_v_64a" : {  #min flow
        "control_switch" : "rhr_v_64a",
        "input" : "rhr_a_discharge_header",
        "output" : StaticTanks.Wetwell,
        "percent_open" : 0,
        "diameter" : 355.60, #mm, 14 in
        "open_speed" : 0.333, #30 seconds to open from full closed.
        "seal_in" : True, 
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },

    "rhr_v_4b" : { 
        "control_switch" : "rhr_v_4b",
        "input" : StaticTanks.Wetwell,
        "output" : "rhr_b_suction_header",
        "percent_open" : 100,
        "diameter" : 609.60, #mm, 24 in
        "open_speed" : 0.0666, #2.5 minutes to open from full closed.
        "seal_in" : True, 
        "sealed_in" : True, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "rhr_v_6b" : { 
        "control_switch" : "rhr_v_6b",
        "input" : StaticTanks.Reactor,
        "output" : "rhr_b_suction_header",
        "percent_open" : 0,
        "diameter" : 609.60, #mm, 24 in
        "open_speed" : 0.0666, #2.5 minutes to open from full closed.
        "seal_in" : True, 
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "rhr_v_48b" : { 
        "control_switch" : "rhr_v_48b",
        "input" : "rhr_b_discharge_header",
        "output" : "rhr_b_main_header",
        "percent_open" : 100,
        "diameter" : 457.20, #mm, 18 in
        "open_speed" : 0.0666, #2.5 minutes to open from full closed.
        "seal_in" : False, 
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "rhr_v_3b" : { 
        "control_switch" : "rhr_v_3b",
        "input" : "rhr_b_discharge_header",
        "output" : "rhr_b_main_header",
        "percent_open" : 100,
        "diameter" : 457.20, #mm, 18 in
        "open_speed" : 0.0666, #2.5 minutes to open from full closed.
        "seal_in" : False, 
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "rhr_v_42b" : { 
        "control_switch" : "rhr_v_42b",
        "input" : "rhr_b_main_header",
        "output" : StaticTanks.Reactor,
        "percent_open" : 0,
        "diameter" : 355.60, #mm, 14 in
        "open_speed" : 0.333, #30 seconds to open from full closed.
        "seal_in" : True, 
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },

    "rhr_v_4c" : { 
        "control_switch" : "rhr_v_4c",
        "input" : StaticTanks.Wetwell,
        "output" : "rhr_c_suction_header",
        "percent_open" : 100,
        "diameter" : 609.60, #mm, 24 in
        "open_speed" : 0.0666, #2.5 minutes to open from full closed.
        "seal_in" : True, 
        "sealed_in" : True, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "rhr_v_42c" : { 
        "control_switch" : "rhr_v_42c",
        "input" : "rhr_c_discharge_header",
        "output" : StaticTanks.Reactor,
        "percent_open" : 0,
        "diameter" : 355.60, #mm, 14 in
        "open_speed" : 0.333, #30 seconds to open from full closed..
        "seal_in" : True, 
        "sealed_in" : False, #current state
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED,
        #TODO: valve control power and motive power
    },
    "rhr_v_24c" : { 
        "control_switch" : "rhr_v_24c",
        "input" : "rhr_c_discharge_header",
        "output" : StaticTanks.Wetwell,
        "percent_open" : 0,
        "diameter" : 355.60, #mm, 14 in
        "open_speed" : 0.333, #30 seconds to open from full closed..
        "seal_in" : True, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    "rhr_v_85b" : { #locally operated
        "control_switch" : "",
        "input" : "rhr_p_3_discharge_header",
        "output" : "rhr_b_discharge_header",
        "percent_open" : 100,
        "diameter" : 355.60, #mm, 14 in
        "open_speed" : 0.333, #30 seconds to open from full closed..
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "rhr_v_85c" : { #locally operated
        "control_switch" : "",
        "input" : "rhr_p_3_discharge_header",
        "output" : "rhr_c_discharge_header",
        "percent_open" : 100,
        "diameter" : 355.60, #mm, 14 in
        "open_speed" : 0.333, #30 seconds to open from full closed..
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    #Nuclear Boiler / Main Steam System

    "nozzle_ms_3a" : { #Main steam line nozzle for MSL B (always 100% open)
        "control_switch" : "",
        "input" : StaticTanks.SteamDome,
        "output" : "main_steam_line_a_drywell",
        "percent_open" : 100,
        "diameter" : 300, #mm, same size as main steam line
        "open_speed" : 0, #Cant change
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "nozzle_ms_3b" : { #Main steam line nozzle for MSL B (always 100% open)
        "control_switch" : "",
        "input" : StaticTanks.SteamDome,
        "output" : "main_steam_line_b_drywell",
        "percent_open" : 100,
        "diameter" : 300, #mm, same size as main steam line
        "open_speed" : 0, #Cant change
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "nozzle_ms_3c" : { #Main steam line nozzle for MSL B (always 100% open)
        "control_switch" : "",
        "input" : StaticTanks.SteamDome,
        "output" : "main_steam_line_c_drywell",
        "percent_open" : 100,
        "diameter" : 300, #mm, same size as main steam line
        "open_speed" : 0, #Cant change
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "nozzle_ms_3d" : { #Main steam line nozzle for MSL B (always 100% open)
        "control_switch" : "",
        "input" : StaticTanks.SteamDome,
        "output" : "main_steam_line_d_drywell",
        "percent_open" : 100,
        "diameter" : 300, #mm, same size as main steam line
        "open_speed" : 0, #Cant change
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    #Reactor Core Isolation Cooling System

    #RCIC PCIS Valves

    "rcic_v_63" : { 
        "control_switch" : "rcic_v_63",
        "input" : "main_steam_line_b_drywell",
        "output" : "rcic_isolation_steam_line",
        "percent_open" : 0,
        "diameter" : 152.40, #mm, 6 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "rcic_v_8" : { 
        "control_switch" : "rcic_v_8",
        "input" : "rcic_isolation_steam_line",
        "output" : "rcic_main_steam_line",
        "percent_open" : 0,
        "diameter" : 152.40, #mm, 6 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    "rcic_v_45" : { 
        "control_switch" : "rcic_v_45",
        "input" : "rcic_main_steam_line",
        "output" : "rcic_turbine_steam_line",
        "percent_open" : 0,
        "diameter" : 152.40, #mm, 6 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "rcic_v_2" : { 
        "control_switch" : "",
        "input" : None,
        "output" : None,
        "percent_open" : 100,
        "diameter" : 101.60, #mm, 4 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "rcic_v_1" : { 
        "control_switch" : "rcic_v_1",
        "input" : "rcic_turbine_steam_line",
        "output" : None,
        "percent_open" : 100,
        "diameter" : 101.60, #mm, 4 inches
        "open_speed" : 10, #1 second to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },


    "rcic_v_68" : { 
        "control_switch" : "rcic_v_68",
        "input" : "rcic_exhaust_steam_line",
        "output" : "magic",
        "percent_open" : 100,
        "diameter" : 200, #mm, 10 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    "rcic_v_13" : { 
        "control_switch" : "rcic_v_13",
        "input" : "rcic_discharge_header",
        "output" : StaticTanks.Reactor,
        "percent_open" : 0,
        "diameter" : 152.40, #mm, 6 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "rcic_v_31" : { 
        "control_switch" : "rcic_v_31",
        "input" : StaticTanks.Wetwell,
        "output" : "rcic_suction_header",
        "percent_open" : 0,
        "diameter" : 203.20, #mm, 8 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    #MSIV Inboard
    "ms_v_22a" : { 
        "control_switch" : "ms_v_22a",
        "input" : "main_steam_line_a_drywell",
        "output" : "main_steam_line_a_penetration",
        "percent_open" : 100,
        "diameter" : 203.20, #mm, 8 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_22b" : { 
        "control_switch" : "ms_v_22b",
        "input" : "main_steam_line_b_drywell",
        "output" : "main_steam_line_b_penetration",
        "percent_open" : 100,
        "diameter" : 203.20, #mm, 8 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_22c" : { 
        "control_switch" : "ms_v_22c",
        "input" : "main_steam_line_c_drywell",
        "output" : "main_steam_line_c_penetration",
        "percent_open" : 100,
        "diameter" : 203.20, #mm, 8 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_22d" : { 
        "control_switch" : "ms_v_22d",
        "input" : "main_steam_line_d_drywell",
        "output" : "main_steam_line_d_penetration",
        "percent_open" : 100,
        "diameter" : 203.20, #mm, 8 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    #MSIV Outboard
    "ms_v_28a" : { 
        "control_switch" : "ms_v_28a",
        "input" : "main_steam_line_a_penetration",
        "output" : "main_steam_line_a_tunnel",
        "percent_open" : 100,
        "diameter" : 203.20, #mm, 8 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_28b" : { 
        "control_switch" : "ms_v_28b",
        "input" : "main_steam_line_b_penetration",
        "output" : "main_steam_line_b_tunnel",
        "percent_open" : 100,
        "diameter" : 203.20, #mm, 8 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_28c" : { 
        "control_switch" : "ms_v_28c",
        "input" : "main_steam_line_c_penetration",
        "output" : "main_steam_line_c_tunnel",
        "percent_open" : 100,
        "diameter" : 203.20, #mm, 8 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_28d" : { 
        "control_switch" : "ms_v_28d",
        "input" : "main_steam_line_d_penetration",
        "output" : "main_steam_line_d_tunnel",
        "percent_open" : 100,
        "diameter" : 203.20, #mm, 8 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    #Main Steam System

    #Nozzles to the Bypass Steam Header

    "nozzle_byp_a" : { #Nozzle for MSL A to the bypass steam header
        "control_switch" : "",
        "input" : "main_steam_line_a_tunnel",
        "output" : "bypass_steam_header",
        "percent_open" : 100,
        "diameter" : 457.20, #mm,
        "open_speed" : 0, #Cant change
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "nozzle_byp_b" : { #Nozzle for MSL A to the bypass steam header
        "control_switch" : "",
        "input" : "main_steam_line_b_tunnel",
        "output" : "bypass_steam_header",
        "percent_open" : 100,
        "diameter" : 457.20, #mm,
        "open_speed" : 0, #Cant change
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "nozzle_byp_c" : { #Nozzle for MSL A to the bypass steam header
        "control_switch" : "",
        "input" : "main_steam_line_c_tunnel",
        "output" : "bypass_steam_header",
        "percent_open" : 100,
        "diameter" : 457.20, #mm,
        "open_speed" : 0, #Cant change
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "nozzle_byp_d" : { #Nozzle for MSL A to the bypass steam header
        "control_switch" : "",
        "input" : "main_steam_line_d_tunnel",
        "output" : "bypass_steam_header",
        "percent_open" : 100,
        "diameter" : 457.20, #mm,
        "open_speed" : 0, #Cant change
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    "the_nothing_nozzle" : { #Sends bypass steam to narnia
        "control_switch" : "",
        "input" : "turbine_bypass_manifold",
        "output" : "magic",
        "percent_open" : 100,
        "diameter" : 400, #mm,
        "open_speed" : 0, #Cant change
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    "the_nothing_nozzle2" : { #Sends turbine steam to narnia
        "control_switch" : "",
        "input" : "fake_turbine",
        "output" : "magic",
        "percent_open" : 100,
        "diameter" : 400, #mm,
        "open_speed" : 0, #Cant change
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    #Bypass Valves

    "ms_v_160a" : { 
        "control_switch" : "",
        "input" : "bypass_steam_header",
        "output" : "turbine_bypass_manifold",
        "percent_open" : 0,
        "diameter" : 254.00, #mm, 8 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_160b" : { 
        "control_switch" : "",
        "input" : "bypass_steam_header",
        "output" : "turbine_bypass_manifold",
        "percent_open" : 0,
        "diameter" : 254.00, #mm, 8 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_160c" : { 
        "control_switch" : "",
        "input" : "bypass_steam_header",
        "output" : "turbine_bypass_manifold",
        "percent_open" : 0,
        "diameter" : 254.00, #mm, 8 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_160d" : { 
        "control_switch" : "",
        "input" : "bypass_steam_header",
        "output" : "turbine_bypass_manifold",
        "percent_open" : 0,
        "diameter" : 254.00, #mm, 8 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    #Governor valves

    "ms_v_gv1" : { 
        "control_switch" : "",
        "input" : "main_steam_line_a_tunnel",
        "output" : "fake_turbine",
        "percent_open" : 0,
        "diameter" : 300, #mm, 28 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_gv2" : { 
        "control_switch" : "",
        "input" : "main_steam_line_b_tunnel",
        "output" : "fake_turbine",
        "percent_open" : 0,
        "diameter" : 300, #mm, 28 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_gv3" : { 
        "control_switch" : "",
        "input" : "main_steam_line_c_tunnel",
        "output" : "fake_turbine",
        "percent_open" : 0,
        "diameter" : 300, #mm, 28 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_gv4" : { 
        "control_switch" : "",
        "input" : "main_steam_line_d_tunnel",
        "output" : "fake_turbine",
        "percent_open" : 0,
        "diameter" : 300, #mm, 28 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },


    #RFT Steam

    "ms_v_105a" : { 
        "control_switch" : "ms_v_105a",
        "input" : "bypass_steam_header",
        "output" : "rft_dt_1a_stop",
        "percent_open" : 100,
        "diameter" : 200,#152.4, #mm, 6 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_172a" : { 
        "control_switch" : "",
        "input" : "rft_dt_1a_stop",
        "output" : "magic",
        "percent_open" : 100,
        "diameter" : 152.4, #mm, 6 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    "ms_v_105b" : { 
        "control_switch" : "ms_v_105b",
        "input" : "bypass_steam_header",
        "output" : "rft_dt_1b_stop",
        "percent_open" : 100,
        "diameter" : 200,#152.4, #mm, 6 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "ms_v_172b" : { 
        "control_switch" : "",
        "input" : "rft_dt_1b_stop",
        "output" : "magic",
        "percent_open" : 100,
        "diameter" : 152.4, #mm, 6 inches
        "open_speed" : 2, #5 seconds to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },


    #Condensate

    "cond_nozzle_hotwell" : { 
        "control_switch" : "",
        "input" : StaticTanks.Hotwell,
        "output" : "condensate_suction",
        "percent_open" : 100,
        "diameter" : 1219.20, #mm, 24 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : False, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    #RFW

    "rfw_v_102a" : { 
        "control_switch" : "rfw_v_102a",
        "input" : "rfw_p_1a_discharge",
        "output" : "rfw_discharge",
        "percent_open" : 0,
        "diameter" : 762, #mm, 24 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "rfw_v_102b" : { 
        "control_switch" : "rfw_v_102b",
        "input" : "rfw_p_1b_discharge",
        "output" : "rfw_discharge",
        "percent_open" : 0,
        "diameter" : 762, #mm, 24 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    #HX
    "rfw_v_108a" : { 
        "control_switch" : "",#"rfw_v_108a",
        "input" : "rfw_discharge",
        "output" : "rfw_hx_6a",
        "percent_open" : 0,
        "diameter" : 762, #mm, 24 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
     "rfw_v_108b" : { 
        "control_switch" : "",#"rfw_v_108b",
        "input" : "rfw_discharge",
        "output" : "rfw_hx_6b",
        "percent_open" : 0,
        "diameter" : 762, #mm, 24 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },

    "rfw_v_112a" : { 
        "control_switch" : "",#"rfw_v_112a",
        "input" : "rfw_hx_6a",
        "output" : "rfw_outlet",
        "percent_open" : 0,
        "diameter" : 762, #mm, 30 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "rfw_v_112b" : { 
        "control_switch" : "",#"rfw_v_112b",
        "input" : "rfw_hx_6b",
        "output" : "rfw_outlet",
        "percent_open" : 0,
        "diameter" : 762, #mm, 30 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : False,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "rfw_v_65a" : { #TODO: Change this to using the HX, bypassing for now to fix a few issues
        "control_switch" : "",#"rfv_v_65a",
        "input" : "rfw_discharge",
        "output" : StaticTanks.Reactor,
        "percent_open" : 100,
        "diameter" : 609.6, #mm, 24 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
    "rfw_v_65b" : { 
        "control_switch" : "",#"rfv_v_65b",
        "input" : "rfw_discharge",
        "output" : StaticTanks.Reactor,
        "percent_open" : 100,
        "diameter" : 609.6, #mm, 24 inches
        "open_speed" : 0.333, #30 seconds to full close to open
        "seal_in" : True, 
        "sealed_in" : True,
        "external_argue" : 0, #0 - No Contest 1 - Wants CLOSED 2 - Wants OPENED
        #TODO: valve control power and motive power
    },
}

def initialize_headers():

    for header_name in headers:
        header = headers[header_name]
        #assume the header is a cylinder
        #so we use pi*r^2
        volume = header["diameter"]/2
        volume = math.pi*(volume**2)
        #then multiply by the height
        volume = volume*header["length"]
        #this stuff is 8th grade math, i hope you know it
        volume = volume/1e6 #to liters
        header["volume"] = volume
        header["mass"] = 1

def valve_inject_to_header(mass:int,header_name):

    if type(header_name) == StaticTanks:
        
        if header_name == StaticTanks.SteamDome:
            #TODO: more than this garbage
            from simulation.models.control_room_columbia.reactor_physics import reactor_inventory
            reactor_inventory.remove_steam(mass*-1)
        else:
            inject_to_static_tank(header_name,mass)
    else:
        headers[header_name]["mass"] += mass
        if headers[header_name]["type"] == FluidTypes.Gas:
            gas.calculate_header_pressure(header_name)
        else:
            calculate_header_pressure(header_name)


def inject_to_header(flow:int,press:int,header_name:str):

    #TODO: feedback to allow pump shutoff head
    header = headers[header_name]
    press = press*6895 # to pascals

    if press > header["pressure"]:
        fluid_flow = calculate_differential_pressure(press,header["pressure"],flow)
        #keep in mind this is in gallons per minute
        mass = fluid_flow*3.785 #to liters per minute
        mass = mass/60 #to per second
        mass = mass*0.1 # sim time
        header["mass"] += mass

        #TODO: change this, we are using the ideal gas law to calculate water, a *liquid* in a pipe.
        from simulation.models.control_room_columbia.reactor_physics import pressure
        header_press = pressure.PartialPressure(pressure.GasTypes["Steam"],24.8,60,header["volume"]-header["mass"])
        header["pressure"] = header_press
        return fluid_flow
    else:
        return 0

def calculate_header_pressure(header_name:str):

    header = headers[header_name]

    from simulation.models.control_room_columbia.reactor_physics import pressure
    header_press = pressure.PartialPressure(pressure.GasTypes["Steam"],24.8,60,header["volume"]-header["mass"])
    header["pressure"] = header_press

def calculate_differential_pressure(pressure_1:int,pressure_2:int,flow:int):

    """Calculates differential pressure vs flow in a system. Can use any units, as long as the pressures are both the same unit."""

    if pressure_2 == 0: pressure_2 = 1

    if pressure_1 > pressure_2:
        pressure_differential = clamp(abs(((pressure_1/pressure_2)-0.3)-1),0,1)
        fluid_flow = pressure_differential*flow

        return fluid_flow
    else:
        return 0

def get_static_tank(name:int):

    match name:
        case StaticTanks.Reactor:
            tank = {}
            from simulation.models.control_room_columbia.reactor_physics import pressure
            tank["pressure"] = pressure.Pressures["Vessel"]+101352.9
            from simulation.models.control_room_columbia.reactor_physics import reactor_inventory
            tank["mass"] = reactor_inventory.waterMass
            tank["type"] = FluidTypes.Liquid,
            return tank
        case StaticTanks.Wetwell:
            tank = {}
            tank["pressure"] = 344738 #50 psi
            tank["mass"] = 10000000
            tank["type"] = FluidTypes.Liquid,
            return tank
        case StaticTanks.SteamDome:
            tank = {}
            from simulation.models.control_room_columbia.reactor_physics import pressure
            tank["pressure"] = pressure.Pressures["Vessel"]
            tank["mass"] = 10000
            tank["type"] = FluidTypes.Gas,
            return tank
        case StaticTanks.Hotwell:
            tank = {}
            tank["pressure"] = 344738 #50 psi
            from simulation.models.control_room_columbia.general_physics import main_condenser
            tank["mass"] = main_condenser.MainCondenserHotwellMass
            tank["type"] = FluidTypes.Liquid,
            return tank

def inject_to_static_tank(name:int,amount):

    match name:
        case StaticTanks.Reactor:
            from simulation.models.control_room_columbia.reactor_physics import reactor_inventory
            reactor_inventory.add_water(amount)
            
    

def get_header(header_name):
    "Can be passed an integer or string. If integer, it will check against the static tanks, and return a formatted table."

    header = {}

    if type(header_name) == StaticTanks:
        header = get_static_tank(header_name)
    else:
        header = headers[header_name]
    
    return header

#this code is garbage
#increment the counter for hours wasted to warn the next guy
#hours wasted = 48

def run():

    for valve_name in valves:
        valve = valves[valve_name]

        if valve["control_switch"] != "":
            if not valve["seal_in"]:
                if model.switches[valve["control_switch"]]["position"] == 2:
                    valve["percent_open"] = min(max(valve["percent_open"]+valve["open_speed"],0),100)
                elif model.switches[valve["control_switch"]]["position"] == 0:
                    valve["percent_open"] = min(max(valve["percent_open"]-valve["open_speed"],0),100)
            elif valve["seal_in"]:
                if len(model.switches[valve["control_switch"]]["positions"]) < 3:
                    if model.switches[valve["control_switch"]]["position"] == 1:
                        valve["sealed_in"] = True
                    elif model.switches[valve["control_switch"]]["position"] == 0:
                        valve["sealed_in"] = False
                else:
                    if model.switches[valve["control_switch"]]["position"] == 2:
                        valve["sealed_in"] = True
                    elif model.switches[valve["control_switch"]]["position"] == 0:
                        valve["sealed_in"] = False
                    
                

                if valve["sealed_in"]:
                    valve["percent_open"] = min(max(valve["percent_open"]+valve["open_speed"],0),100)
                else:
                    valve["percent_open"] = min(max(valve["percent_open"]-valve["open_speed"],0),100)

            if model.switches[valve["control_switch"]]["lights"] != {}:
                model.switches[valve["control_switch"]]["lights"]["green"] = valve["percent_open"] < 100
                model.switches[valve["control_switch"]]["lights"]["red"] = valve["percent_open"] > 0

        if valve["input"] == None or valve["output"] == None or valve["output"] == "magic":
            continue

        inlet = get_header(valve["input"])
        outlet = get_header(valve["output"])

        if inlet["type"] == FluidTypes.Gas or outlet["type"] == FluidTypes.Gas:
            continue #this is handled by gas.py


        #Poiseuille's law
        #Q = π(P₁ – P₂)r⁴ / 8μL.
        #where,
        #Q is the volumetric flow rate,
        #P1 and P2 are the pressures at both ends of the pipe,
        #r is the radius of the pipe,
        #μ is the viscosity of the fluid,
        #L is the length of the pipe.

        #viscosity of water is 0.01 poise
        #placeholder 20000 mm as length (so 20 cm)

        if valve_name == "rhr_v_6b" or valve_name == "rhr_v_6a": #override the inlets for SDC to have more pressure so there is sufficient head
            inlet["pressure"] = 1.379e6

        radius = valve["diameter"]/2
        radius = radius*0.1 #to cm

        #flow_resistance = (8*33*1000)/(math.pi*(radius**4))
        flow_resistance = (8*33*3.3*1000)/(math.pi*(radius**4))

        #flow = math.pi*((inlet["pressure"]*0.001)-(outlet["pressure"]*0.001))*(radius**4)/(8*0.01*200)

        flow = (inlet["pressure"]-outlet["pressure"])/flow_resistance
        flow = abs(flow)

        flow = flow*(valve["percent_open"]/100) #TODO: Exponents? Flow is not linear.
        #flow is in cubic centimeters per second
        flow = flow/1000 #to liter/s
        flow = flow*0.1

        if type(valve["output"]) == str:
                if outlet["mass"] + flow >= outlet["volume"]:
                    flow = max(outlet["volume"]-(outlet["mass"] + flow),0)

        valve["flow"] = flow

        if inlet["pressure"] < outlet["pressure"] or inlet["mass"] < 0:
            #valve_inject_to_header(flow,valve["input"])
            #valve_inject_to_header(flow*-1,valve["output"])
            valve["flow"] = 0
            continue
        else:
            valve_inject_to_header(flow*-1,valve["input"])
            valve_inject_to_header(flow,valve["output"])

        inlet["mass"] = max(0,inlet["mass"])
