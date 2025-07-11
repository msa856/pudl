"""Metadata for cleaning, re-encoding, and documenting coded data columns.

These dictionaries are used to create Encoder instances. Each key is a table name with
a sub dictionary that includes additional detail. The table names must end with the
data_source as a sufix (for EIA 860, 861 or 923 tables include ``_eia``).

The table-specific dictionaries contain the following keys:

* 'df': A dataframe associating short codes with long descriptions and other information.
  Each dataframe needs at least three standard columns: "code", "label", "description".
  The codes and lables must be unique. By convention, the "label"'s are snake case.
* 'code_fixes': A dictionary mapping non-standard codes to canonical, standardized
  codes.
* 'ignored_codes': A list of non-standard codes which appear in the data, and will
  be set to NA.
"""

from io import StringIO
from typing import Any

import numpy as np
import pandas as pd

CODE_METADATA: dict[str, dict[str, Any]] = {
    "core_eia__codes_boiler_status": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("CN", "cancelled", "Cancelled (previously reported as “planned”)."),
                ("CO", "under_construction", "A new unit under construction."),
                (
                    "OP",
                    "operating",
                    "In commercial service or out of service less than 365 days.",
                ),
                ("OS", "out_of_service", "Out of service for 365 days or longer."),
                (
                    "PL",
                    "planned",
                    "Expected to go into commercial service within 10 years.",
                ),
                (
                    "RE",
                    "retired",
                    "No longer in service and not expected to be returned to service.",
                ),
                (
                    "SB",
                    "standby",
                    "Standby or inactive reserve; i.e., not normally used, but available for service",
                ),
                (
                    "SC",
                    "cold_standby",
                    "Cold standby or reserve; deactivated (usually requires 3 to 6 months to reactivate)",
                ),
                (
                    "TS",
                    "test",
                    "Operating under test conditions (not in commercial service)",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {
            "op": "OP",
            "re": "RE",
            "OA": "OP",
            "IP": "CN",
            "R": "RE",
            "P": "PL",
            "V": "CO",
            "ts": "TS",
        },
        "ignored_codes": [0, "OC", "T", "0", "df"],
    },
    "core_eia__codes_boiler_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "D",
                    "nps_post_1971",
                    "Standards of Performance for fossil-fuel fired steam boilers for which construction began after August 17, 1971.",
                ),
                (
                    "Da",
                    "nps_post_1978",
                    "Standards of Performance for fossil-fuel fired steam boilers for which construction began after September 18, 1978.",
                ),
                (
                    "Db",
                    "nps_post_1984",
                    "Standards of Performance for fossil-fuel fired steam boilers for which construction began after June 19, 1984.",
                ),
                (
                    "Dc",
                    "nps_small_units",
                    "Standards of Performance for small industrial-commercial-institutional steam generating units.",
                ),
                (
                    "N",
                    "not_covered",
                    "Not covered under New Source Performance Standards.",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_eia__codes_coalmine_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("P", "preparation_plant", "A coal preparation plant."),
                ("S", "surface", "A surface mine."),
                ("U", "underground", "An underground mine."),
                (
                    "US",
                    "underground_and_surface",
                    (
                        "Both an underground and surface mine with most coal extracted "
                        "from underground"
                    ),
                ),
                (
                    "SU",
                    "surface_and_underground",
                    (
                        "Both an underground and surface mine with most coal extracted "
                        "from surface"
                    ),
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {
            "p": "P",
            "U/S": "US",
            "S/U": "SU",
            "Su": "S",
        },
        "ignored_codes": [],
    },
    "core_eia__codes_environmental_equipment_manufacturers": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("AA", "advanced_air_technologies", "Advanced Air Technologies"),
                ("AB", "advanced_burnertechnologies", "Advanced Burner Technologies"),
                ("ABB", "abb_environmental_systems", "ABB Environmental Systems"),
                (
                    "AC",
                    "advanced_combustion_technology",
                    "Advanced Combustion Technology",
                ),
                ("AEE", "aee_von_roll", "AEE Von Roll"),
                (
                    "AES",
                    "alliant_environmental_solutions",
                    "Alliant Environmental Solutions",
                ),
                ("AI", "aalborg_industries", "Aalborg Industries"),
                ("AL", "alstom", "Alstom"),
                ("AM", "american_air_filter", "American Air Filter"),
                ("AN", "andritz", "Andritz"),
                ("AP", "airpol", "AirPol"),
                ("API", "air_pollution_industries", "Air Polution Industries"),
                ("AS", "american_shack", "American Shack"),
                ("AT", "applied_thermal_systems", "Applied Thermal Systems"),
                ("AU", "applied_utility_systems", "Applied Utility Systems (AUS)"),
                ("AX", "amerex_industries", "Amerex Industries"),
                ("AZ", "alzeta", "Alzeta"),
                ("BC", "babcock_borsig_power", "Babcock Borsig Power"),
                ("BE", "bact_engineering", "Bact Engineering"),
                ("BI", "bleco_industries", "Bleco Industries"),
                ("BL", "bechtel_corporation", "Bechtel Corporation"),
                ("BM", "bloom", "Bloom"),
                ("BMD", "burns_mcdonnell", "Burns & McDonnell"),
                ("BO", "bionomics", "Bionomics"),
                ("BPC", "belco_pollution_control", "Belco Pollution Control"),
                (
                    "BPE",
                    "babcock_power_environmental_inc",
                    "Babcock Power Environmental Inc (BPEI)",
                ),
                ("BR", "bros", "BROS"),
                ("BT", "belco_technologies", "Belco Technologies"),
                ("BW", "babcock_wilcox", "Babcock and Wilcox"),
                ("CA", "chiyoda", "Chiyoda"),
                ("CB", "clyde_bergeman_eec", "Clyde Bergeman EEC"),
                ("CC", "chemico", "Chemico"),
                ("CE", "combustion_engineering", "Combustion Engineering"),
                (
                    "CM",
                    "combustion_components_associates_inc",
                    "Combustion Components Associates Inc",
                ),
                ("CMI", "cmi", "CMI"),
                ("CN", "coen", "Coen"),
                ("CO", "combustion_equipment", "Combustion Equipment"),
                ("CSI", "combustion_solutions_inc", "Combustion Solutions Inc"),
                ("CT", "callidus_technologies", "Callidus Technologies"),
                ("DA", "delta_conveying_systems", "Delta Conveying Systems"),
                ("DB", "deutsche_babcock", "Deutsche-Babcock"),
                ("DC", "ducon", "Ducon"),
                ("DD", "damper_design_inc", "Damper Design Inc"),
                ("DJ", "de_jong_coen_bv", "De Jong Coen bv"),
                ("DL", "deltak", "Deltak"),
                ("DM", "davey_mckee", "Davey McKee"),
                (
                    "DQ",
                    "duquense",
                    "Duquense Light Company & Energy Systems Associates",
                ),
                ("DS", "doosan", "Doosan"),
                ("DV", "davis", "Davis"),
                ("DX", "deltex", "Deltex"),
                ("EA", "eagle_air", "Eagle Air"),
                ("EC", "econotherm", "Econotherm"),
                ("EE", "environmental_engineering", "Environmental Engineering"),
                (
                    "EEC",
                    "environmental_elements_corp",
                    "Environmental Elements Corporation",
                ),
                (
                    "EG",
                    "energy_environmental_research_corp",
                    "Energy and Environmental Research Corp (EER)",
                ),
                ("EI", "entollter_inc", "Entollter Inc"),
                ("EL", "electric_power_technologies", "Electric Power Technologies"),
                ("EP", "epri", "EPRI"),
                ("EPI", "energy_products_idaho", "Energy Products of Idaho"),
                ("ER", "eerie_city_iron_works", "Eerie City Iron Works"),
                ("ET", "entek", "Entek"),
                (
                    "ETE",
                    "entropy_technology",
                    "Entropy Technology and Environmental Consultants (ETEC Inc)",
                ),
                ("FB", "faber", "Faber"),
                ("FL", "flakt_inc", "Flakt Inc"),
                ("FM", "fmc", "FMC"),
                ("FN", "forney", "Forney"),
                ("FT", "fuel_tech_inc", "Fuel Tech Inc"),
                ("FW", "foster_wheeler", "Foster Wheeler"),
                ("GE", "general_electric", "General Electric"),
                ("GF", "grafwolff", "Grafwolff"),
                (
                    "GR",
                    "ge_energy",
                    "GE Energy and Environmental Research Corp (GEEER)",
                ),
                ("GT", "gotaverken", "Gotaverken"),
                ("HA", "hamon", "Hamon"),
                ("HL", "holman", "Holman"),
                ("HT", "hitachi", "Hitachi"),
                (
                    "IC",
                    "international_combustion_ltd",
                    "International Combustion Limited",
                ),
                ("ID", "indeck", "Indeck"),
                ("IH", "in_house_design", "In house design"),
                (
                    "IHI",
                    "ishikawajima_harima",
                    "Ishikawajima-Harima Heavy Industries  (IHI Corp)",
                ),
                ("IS", "innovative_steam_technology", "Innovative Steam Technology"),
                ("JO", "joy_manufacturing", "Joy Manufacturing"),
                (
                    "JZ",
                    "john_zink_todd_combustion",
                    "John Zink Todd Combustion/Todd Combustion",
                ),
                ("KC", "korea_cottrell", "Korea Cottrell"),
                ("KE", "m_w_kellogg", "M. W. Kellogg"),
                ("KL", "keeler_dorr_oliver", "Keeler Dorr Oliver"),
                ("KP", "kvaerner_pulping", "Kvaerner Pulping"),
                ("KR", "krebs_engineers", "Krebs Engineers"),
                ("KW", "kawasaki_heavy_industries", "Kawaski Heavy Industries"),
                ("LLB", "lurgi_lentjes_bischoff", "Lurgi Lentjes Bischoff"),
                ("MB", "mitsui_babcock", "Mitsui-Babcock"),
                ("MC", "macrotek", "Macrotek"),
                ("ME", "mitchell_engineering", "Mitchell Engineering"),
                ("MG", "mcgill_air_clean", "McGill Air Clean"),
                ("MI", "mitsubishi_heavy_industries", "Mitsubishi Heavy Industries"),
                ("MK", "merrick_industries", "Merrick Industries"),
                ("MT", "mobotec", "Mobotec"),
                ("MX", "marselex", "Marselex"),
                ("NB", "nebraska_boiler", "Nebraska Boiler"),
                ("NC", "natcom_inc", "Natcom Inc"),
                ("NE", "nei", "NEI"),
                ("NL", "noell_inc", "Noell Inc"),
                ("NM", "nem", "NEM"),
                ("NPA", "neptune_airpol", "Neptune Airpol"),
                ("NSP", "nsp", "NSP"),
                ("NT", "nooter_erickson", "Nooter Erickson"),
                (
                    "OT",
                    "other",
                    "Other (specify in a Footnote on SCHEDULE 7, COMMENTS)",
                ),
                ("PA", "procedair", "Procedair"),
                ("PB", "peabody", "Peabody"),
                ("PI", "power_and_industrial", "Power and Industrial"),
                ("PL", "pillard", "Pillard"),
                ("PPC", "ppc_industries", "PPC Industries"),
                ("PR", "pyro_power", "Pyro Power"),
                ("PS", "peerless_manufacturing_co", "Peerless Manufacturing Company"),
                ("PU", "pure_air", "Pure Air"),
                ("PX", "phoenix_combustion", "Phoenix Combustion"),
                ("RC", "research_cottrell", "Research Cottrell"),
                ("RD", "rodenhuis_verloop", "Rodenhuis and Verloop"),
                ("RI", "riley", "Riley"),
                ("RJ", "rjm", "RJM"),
                ("RR", "rolls_royce", "Rolls Royce"),
                ("RS", "riley_stoker", "Riley-Stoker/Riley Power"),
                ("RV", "rv_industries", "RV Industries"),
                ("SB", "smartburn", "SmartBurn"),
                ("SC", "southern_co", "Southern Company"),
                (
                    "SHU",
                    "saarberg_holter_umweltechnick",
                    "Saarberg-Holter Umweltechnick GmbH",
                ),
                ("SK", "schenck_weigh_feeders", "Schenck Weigh Feeders"),
                ("SM", "smoot_co", "Smoot Company"),
                ("ST", "sterling", "Sterling"),
                ("SW", "siemens_westinghouse", "Siemens-Westinghouse"),
                ("TC", "turbosonic", "Turbosonic"),
                ("TEC", "thermal_equipment_corp", "Thermal Equipment Corporation"),
                ("TH", "thyssen_cea", "Thyssen/CEA"),
                ("TK", "turbotak", "Turbotak"),
                ("TM", "tampella_power_corp", "Tampella Power Corporation"),
                ("TP", "tempala_power", "Tempala Power"),
                ("TS", "toshiba", "Toshiba"),
                ("UE", "utility_engineering", "Utility Engineering"),
                ("UM", "united_mcgill", "United McGill"),
                ("UO", "universal_oil_products", "Universal Oil Products"),
                ("VO", "vogt", "Vogt Machine Company/Vogt Power"),
                (
                    "WAP",
                    "wheelabrator_air_pollution_control",
                    "Wheelabrator Air Pollution Control",
                ),
                ("WE", "westinghouse", "Westinghouse"),
                ("WG", "weigl_engineering", "Weigl Engineering"),
                ("WI", "wickes", "Wickes"),
                ("ZC", "zeeco", "Zeeco"),
                ("ZN", "zurn", "Zurn"),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": ["NA", "IN", "WA"],
    },
    "core_eia__codes_emission_control_equipment_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "ACI",
                    "activated_carbon_injection",
                    "Activated carbon injection system",
                ),
                ("BP", "baghouse_pulse", "Baghouse (fabric filter), pulse"),
                (
                    "BR",
                    "baghouse_reverse_air",
                    "Baghouse (fabric filter), reverse air",
                ),
                (
                    "BS",
                    "baghouse_shake_deflate",
                    "Baghouse (fabric filter), shake and deflate",
                ),
                ("CD", "circulating_dry_scrubber", "Circulating dry scrubber"),
                (
                    "DSI",
                    "dry_sorbent_injection",
                    "Dry sorbent (powder) injection type",
                ),
                (
                    "EC",
                    "electrostatic_cold_conditioned",
                    "Electrostatic precipitator, cold side, with flue gas conditioning",
                ),
                (
                    "EH",
                    "electrostatic_hot_conditioned",
                    "Electrostatic precipitator, hot side, with flue gas conditioning",
                ),
                (
                    "EK",
                    "electrostatic_cold_unconditioned",
                    "Electrostatic precipitator, cold side, without flue gas conditioning",
                ),
                (
                    "EW",
                    "electrostatic_hot_unconditioned",
                    "Electrostatic precipitator, hot side, without flue gas conditioning",
                ),
                (
                    "JB",
                    "wet_scrubber_jet_bubbling",
                    "Jet bubbling reactor (wet) scrubber",
                ),
                ("LIJ", "lime_injection", "Lime injection"),
                ("LNB", "low_nox_burner", "Low NOx burner"),
                (
                    "MA",
                    "wet_scrubber_mechanical",
                    "Mechanically aided type (wet) scrubber",
                ),
                ("MC", "multiple_cyclone", "Multiple cyclone"),
                ("OT", "other", "Other"),
                ("PA", "wet_scrubber_packed", "Packed type (wet) scrubber"),
                ("SC", "single_cyclone", "Single cyclone"),
                (
                    "SD",
                    "spray_dryer",
                    "Spray dryer type / dry FGD / semi-dry FGD",
                ),
                (
                    "SN",
                    "selective_noncatalytic_reduction",
                    "Selective noncatalytic reduction",
                ),
                ("SP", "wet_scrubber_spray", "Spray type (wet) scrubber"),
                (
                    "SR",
                    "selective_catalytic_reduction",
                    "Selective catalytic reduction",
                ),
                ("TR", "wet_scrubber_tray", "Tray type (wet) scrubber"),
                ("VE", "wet_scrubber_venturi", "Venturi type (wet) scrubber."),
            ],
        ).convert_dtypes(),
        "code_fixes": {
            "SR-2": "SR",
            "sn": "SN",
            "LN": "LNB",
            "DP": "DSI",
        },
        "ignored_codes": ["HRSG1", "HRSG2", "FGD", "OV"],
    },
    "core_eia__codes_firing_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("CB", "cell_burner", "A boiler with a cell burner."),
                ("CY", "cyclone_firing", "A cyclone-fired boiler."),
                ("DB", "duct_burner", "A boiler with a duct burner."),
                (
                    "FB",
                    "fluidized_bed_firing",
                    "A boiler with fluidized bed firing (circulating fluidized bed, bubbling fluidized bed).",
                ),
                (
                    "SS",
                    "stoker",
                    "A stoker-fired boiler (spreader, vibrating Gate, slinger).",
                ),
                (
                    "TF",
                    "tangential_firing",
                    "A boiler with tangential, concentric or corner firing.",
                ),
                ("VF", "vertical_firing", "A vertical or arch-fired boiler."),
                (
                    "WF",
                    "wall_fired",
                    "A wall-fired boiler (opposed wall, rear wall, front wall, side wall).",
                ),
                ("OT", "other", "Other: specify in Schedule 7."),
            ],
        ).convert_dtypes(),
        "code_fixes": {
            "AF": "VF",
            "CF": "TF",
            "FF": "WF",
            "OF": "WF",
            "RF": "WF",
            "SF": "WF",
        },
        "ignored_codes": [],
    },
    "core_eia__codes_nox_compliance_strategies": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("AA", "advanced_overfire_air", "Advanced overfire air."),
                ("BF", "biased_firing", "Biased firing (alternative burners)."),
                ("CF", "fluidized_bed_combustor", "Fluidized bed combustor."),
                ("FR", "flue_gas_recirculation", "Flue gas recirculation."),
                ("FU", "fuel_reburning", "Fuel reburning."),
                ("H2O", "water_injection", "Water injection."),
                ("LA", "low_excess_air", "Low excess air."),
                ("LN", "low_nox_burner", "Low NOx burner."),
                ("NH3", "ammonia_injection", "Ammonia injection."),
                (
                    "NC",
                    "no_change",
                    "No change in historic operation of unit anticipated.",
                ),
                ("ND", "not_determined", "Not determined at this time."),
                ("OV", "overfire_air", "Overfire air."),
                ("RP", "repower_unit", "Repower unit."),
                ("SC", "slagging", "Slagging."),
                ("SN", "noncatalytic_reduction", "Selective noncatalytic reduction."),
                ("SR", "catalytic_reduction", "Selective catalytic reduction."),
                ("STM", "steam_injection", "Steam injection."),
                (
                    "UE",
                    "decrease_utilization",
                    "Decrease utilization; rely on energy conservation and/or improved efficiency.",
                ),
                ("OT", "other", "Other: specify in Schedule 7."),
                ("BO", "out_of_service", "Burner out of service."),
                ("MS", "meeting_standard", "Boiler currently meeting standard."),
                ("NP", "no_plans", "No plans to control."),
                (
                    "SE",
                    "seeking_revision",
                    "Seeking revision of government regulation.",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {"H2": "H2O", "NH": "NH3", "ST": "STM", "ln": "LN"},
        "ignored_codes": ["NA"],
    },
    "core_eia__codes_nox_control_status": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("CN", "cancelled", "Cancelled (previously reported as planned)"),
                ("CO", "under_construction", "A new unit under construction."),
                (
                    "OP",
                    "operating",
                    "In commercial service or out of service less than 365 days.",
                ),
                ("OS", "out_of_service", "Out of service for 365 days or longer."),
                ("OZ", "ozone_season", "Operating during the ozone season."),
                (
                    "PL",
                    "planned",
                    "Planned.",
                ),
                (
                    "RE",
                    "retired",
                    "No longer in service and not expected to be returned to service.",
                ),
                (
                    "SB",
                    "standby",
                    "Standby or inactive reserve.",
                ),
                (
                    "SC",
                    "cold_standby",
                    "Cold standby or reserve.",
                ),
                (
                    "TS",
                    "test",
                    "Operating under test conditions.",
                ),
                ("NC", "no_plans", "No plans to control."),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": ["NA"],
    },
    "core_eia__codes_nox_units": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("NH", "lbs_per_hour", "Pounds of nitrogen oxides emitted per hour."),
                (
                    "NL",
                    "declining_level",
                    "Annual nitrogen oxides emission level less than a level in a previous year.",
                ),
                (
                    "NM",
                    "ppm_stack_gas",
                    "Parts per million of nitrogen oxides in stack gas.",
                ),
                (
                    "NO",
                    "ambient_air_quality",
                    "Ambient air quality concentration of nitrogen oxides (parts per million).",
                ),
                (
                    "NP",
                    "lbs_per_mmbtu_fuel",
                    "Pounds of nitrogen oxides per mmbtu in fuel.",
                ),
                ("OT", "other", "Other: specify in schedule 7."),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_eia__codes_averaging_periods": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("NV", "never_to_exceed", "Never to exceed."),
                ("FM", "5_min", "Five minutes."),
                ("SM", "six_min", "Six minutes."),
                ("FT", "fifteen_min", "Fifteen minutes."),
                ("OH", "one_hr", "One hour."),
                ("WO", "two_hrs", "Two hours."),
                ("TH", "three_hrs", "Three hours."),
                ("EH", "eight_hrs", "Eight hours."),
                ("DA", "one_day", "24 hours."),
                ("WA", "one_week", "One week."),
                ("MO", "thirty_days", "30 days."),
                ("ND", "ninety_days", "90 days."),
                ("YR", "annual", "Annual."),
                ("PS", "periodic", "Periodic stack testing."),
                ("DT", "defined_by_testing", "Defined by testing."),
                ("NS", "not_specified", "Not specified."),
                ("OT", "other", "Other: specify in schedule 7."),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_eia__codes_particulate_compliance_strategies": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("BO", "out_of_service", "Burner out of service."),
                ("FR", "flue_gas_recirculation", "Flue gas recirculation."),
                ("LA", "low_excess_air", "Low excess air."),
                ("LN", "low_nox_burner", "Low NOx burner."),
                ("MS", "meeting_standard", "Boiler currently meeting standard."),
                ("NC", "no_plans", "No plans to control."),
                ("OV", "overfire_air", "Overfire air."),
                ("OT", "other", "Other: specify in Schedule 7."),
                (
                    "SE",
                    "seeking_revision",
                    "Seeking revision of government regulation.",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_eia__codes_particulate_units": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "OP",
                    "pct_opacity",
                    "Percent of opacity.",
                ),
                (
                    "PB",
                    "lbs_per_mmbtu_fuel",
                    "Pounds of particulate matter per million Btu in fuel.",
                ),
                (
                    "PC",
                    "grains_per_cf_stack_gas",
                    "Grains of particulate matter per standard cubic foot of stack gas.",
                ),
                (
                    "PG",
                    "lbs_per_thousand_lbs_stack_gas",
                    "Pounds of particulate matter per thousand pounds of stack gas.",
                ),
                (
                    "PH",
                    "lbs_per_hour",
                    "Pounds of particulate matter emitted per hour.",
                ),
                (
                    "UG",
                    "mcg_per_m3",
                    "Micrograms of particulate matter per cubic meter.",
                ),
                ("OT", "other", "Other: specify in schedule 7."),
            ],
        ).convert_dtypes(),
        "code_fixes": {"DP": "PB"},
        "ignored_codes": [],
    },
    "core_ferc1__codes_power_purchase_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "AD",
                    "adjustment",
                    (
                        "Out-of-period adjustment. Use this code for any accounting "
                        "adjustments or 'true-ups' for service provided in prior "
                        "reporting years. Provide an explanation in a footnote for "
                        "each adjustment."
                    ),
                ),
                (
                    "EX",
                    "electricity_exchange",
                    (
                        "Exchanges of electricity. Use this category for transactions "
                        "involving a balancing of debits and credits for energy, "
                        "capacity, etc.  and any settlements for imbalanced exchanges."
                    ),
                ),
                (
                    "IF",
                    "intermediate_firm",
                    (
                        "Intermediate-term firm service. The same as LF service expect "
                        "that 'intermediate-term' means longer than one year but less"
                        "than five years."
                    ),
                ),
                (
                    "IU",
                    "intermediate_unit",
                    'Intermediate-term service from a designated generating unit. The same as LU service expect that "intermediate-term" means longer than one year but less than five years.',
                ),
                (
                    "LF",
                    "long_firm",
                    'Long-term firm service. "Long-term" means five years or longer and "firm" means that service cannot be interrupted for economic reasons and is intended to remain reliable even under adverse conditions (e.g., the supplier must attempt to buy emergency energy from third parties to maintain deliveries of LF service). This category should not be used for long-term firm service firm service which meets the definition of RQ service. For all transaction identified as LF, provide in a footnote the termination date of the contract defined as the earliest date that either buyer or seller can unilaterally get out of the contract.',
                ),
                (
                    "LU",
                    "long_unit",
                    'Long-term service from a designated generating unit. "Long-term" means five years or longer. The availability and reliability of service, aside from transmission constraints, must match the availability and reliability of the designated unit.',
                ),
                (
                    "OS",
                    "other_service",
                    "Other service. Use this category only for those services which cannot be placed in the above-defined categories, such as all non-firm service regardless of the Length of the contract and service from designated units of Less than one year. Describe the nature of the service in a footnote for each adjustment.",
                ),
                (
                    "RQ",
                    "requirement",
                    "Requirements service. Requirements service is service which the supplier plans to provide on an ongoing basis (i.e., the supplier includes projects load for this service in its system resource planning). In addition, the reliability of requirement service must be the same as, or second only to, the supplier’s service to its own ultimate consumers.",
                ),
                (
                    "SF",
                    "short_firm",
                    "Short-term service. Use this category for all firm services, where the duration of each period of commitment for service is one year or less.",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [
            "",
            "To",
            'A"',
            'B"',
            'C"',
            "ÿ\x16",
            "NA",
            " -",
            "-",
            "OC",
            "N/",
            "Pa",
            "0",
        ],
    },
    "core_eia__codes_momentary_interruptions": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "L",
                    "less_than_1_minute",
                    "Respondent defines a momentary interruption as less than 1 minute.",
                ),
                (
                    "F",
                    "less_than_5_minutes",
                    "Respondent defines a momentary interruption as less than 5 minutes.",
                ),
                (
                    "O",
                    "other",
                    "Respondent defines a momentary interruption using some other criteria.",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {"5": "F"},
        "ignored_codes": [],
    },
    "core_eia__codes_boiler_generator_assn_types": {
        "df": pd.DataFrame(
            columns=[
                "code",
                "label",
                "description",
            ],
            data=[
                ("A", "actual", "An actual boiler generator association."),
                ("T", "theoretical", "A theoretical boiler generator association."),
            ],
        ),
        "code_fixes": {"t": "T", "a": "A"},
        "ignored_codes": ["1"],
    },
    "core_eia__codes_operational_status": {
        "df": pd.DataFrame(
            columns=["code", "label", "description", "operational_status"],
            data=[
                (
                    "CN",
                    "cancelled",
                    "Cancelled, but previously reported as 'planned'",
                    "proposed",
                ),
                (
                    "CO",
                    "under_construction",
                    "New unit under construction.",
                    "proposed",
                ),
                (
                    "IP",
                    "indefinitely_postponed",
                    "Planned new indefinitely postponed, or no longer in resource plan",
                    "proposed",
                ),
                (
                    "L",
                    "planned_approvals_pending",
                    "Not under construction but site preparation could be underway",
                    "proposed",
                ),
                (
                    "OA",
                    "out_of_service_short_term",
                    "Was not used for some or all of the reporting period but is expected to be returned to service in the next calendar year.",
                    "existing",
                ),
                (
                    "OP",
                    "operating",
                    "Operating (in commercial service or out of service within 365 days). For generators, this means in service (commercial operation) and producing some electricity. Includes peaking units that are run on an as needed (intermittent or seasonal) basis.",
                    "existing",
                ),
                (
                    "OS",
                    "out_of_service_long_term",
                    "Was not used for some or all of the reporting period and is NOT expected to be returned to service in the next calendar year.",
                    "existing",
                ),
                (
                    "OT",
                    "other",
                    "proposed",
                    "proposed",
                ),
                (
                    "OZ",
                    "operate_during_ozone_season",
                    "Operated only during the ozone season (May through September). Only used for emissions equipment.",
                    "existing",
                ),
                (
                    "P",
                    "planned_approvals_not_initiated",
                    "Planned for installation but regulatory approvals not initiated; Not under construction",
                    "proposed",
                ),
                (
                    "PL",
                    "planned",
                    "Planned (expected to go into commercial service within 10 years)",
                    "proposed",
                ),
                (
                    "RE",
                    "retired",
                    "No longer in service and not expected to be returned to service.",
                    "retired",
                ),
                (
                    "SB",
                    "standby",
                    "Standby/Backup. Available for service but not normally used (has little or no generation during the year) for this reporting period. Includes old code BU from 2004-2006.",
                    "existing",
                ),
                (
                    "SC",
                    "standby_col",
                    "Cold Standby (Reserve); deactivated. Usually requires 3 to 6 months to reactivate",
                    "existing",
                ),
                (
                    "T",
                    "planned_approvals_received",
                    "Regulatory approvals received. Not under construction but site preparation could be underway",
                    "proposed",
                ),
                (
                    "TS",
                    "construction_complete",
                    "Construction complete, but not yet in commercial operation (including low power testing of nuclear units). Operating under test conditions.",
                    "proposed",
                ),
                (
                    "U",
                    "under_construction_less_than_half_complete",
                    "Under construction, less than or equal to 50 percent complete (based on construction time to date of operation)",
                    "proposed",
                ),
                (
                    "V",
                    "under_construction_more_than_half_complete",
                    "Under construction, more than 50 percent complete (based on construction time to date of operation)",
                    "proposed",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {
            "(L) Regulatory approvals pending. Not under construction": "L",
            "(OA) Out of service but expected to return to service in next calendar year": "OA",
            "(OP) Operating": "OP",
            "(OS) Out of service and NOT expected to return to service in next calendar year": "OS",
            "(OT) Other": "OT",
            "(P) Planned for installation, but regulatory approvals not initiated": "P",
            "(SB) Standby/Backup: available for service but not normally used": "SB",
            "(T) Regulatory approvals received. Not under construction": "T",
            "(TS) Construction complete, but not yet in commercial operation": "TS",
            "(U) Under construction, less than or equal to 50 percent complete": "U",
            "(V) Under construction, more than 50 percent complete": "V",
            "BU": "SB",
        },
        "ignored_codes": ["CS"],
    },
    "core_eia__codes_energy_sources": {
        "df": pd.DataFrame(
            columns=[
                "code",
                "label",
                "fuel_units",
                "min_fuel_mmbtu_per_unit",
                "max_fuel_mmbtu_per_unit",
                "fuel_group_eia",
                "fuel_derived_from",
                "fuel_phase",
                "fuel_type_code_pudl",
                "description",
            ],
            data=[
                (
                    "AB",
                    "agricultural_byproducts",
                    "short_tons",
                    7.0,
                    18.0,
                    "renewable",
                    "biomass",
                    "solid",
                    "waste",
                    "Agricultural by-products",
                ),
                (
                    "ANT",
                    "anthracite",
                    "short_tons",
                    22.0,
                    28.0,
                    "fossil",
                    "coal",
                    "solid",
                    "coal",
                    "Anthracite coal",
                ),
                (
                    "BFG",
                    "blast_furnace_gas",
                    "mcf",
                    0.07,
                    0.12,
                    "fossil",
                    "gas",
                    "gas",
                    "gas",
                    "Blast furnace gas",
                ),
                (
                    "BIT",
                    "bituminous_coal",
                    "short_tons",
                    20.0,
                    29.0,
                    "fossil",
                    "coal",
                    "solid",
                    "coal",
                    "Bituminous coal",
                ),
                (
                    "BLQ",
                    "black_liquor",
                    "short_tons",
                    10.0,
                    14.0,
                    "renewable",
                    "biomass",
                    "liquid",
                    "waste",
                    "Black liquor",
                ),
                (
                    "DFO",
                    "distillate_fuel_oil",
                    "barrels",
                    5.5,
                    6.2,
                    "fossil",
                    "petroleum",
                    "liquid",
                    "oil",
                    "Distillate fuel oil, including diesel, No. 1, No. 2, and No. 4 fuel oils",
                ),
                (
                    "GEO",
                    "geothermal",
                    pd.NA,
                    np.nan,
                    np.nan,
                    "renewable",
                    "other",
                    pd.NA,
                    "other",
                    "Geothermal",
                ),
                (
                    "JF",
                    "jet_fuel",
                    "barrels",
                    5.0,
                    6.0,
                    "fossil",
                    "petroleum",
                    "liquid",
                    "oil",
                    "Jet fuel",
                ),
                (
                    "KER",
                    "kerosene",
                    "barrels",
                    5.6,
                    6.1,
                    "fossil",
                    "petroleum",
                    "liquid",
                    "oil",
                    "Kerosene",
                ),
                (
                    "LFG",
                    "landfill_gas",
                    "mcf",
                    0.3,
                    0.6,
                    "renewable",
                    "biomass",
                    "gas",
                    "waste",
                    "Landfill gas",
                ),
                (
                    "LIG",
                    "lignite",
                    "short_tons",
                    10.0,
                    14.5,
                    "fossil",
                    "coal",
                    "solid",
                    "coal",
                    "Lignite coal",
                ),
                (
                    "MSB",
                    "municipal_solid_waste_biogenic",
                    "short_tons",
                    9.0,
                    12.0,
                    "renewable",
                    "biomass",
                    "solid",
                    "waste",
                    "Municipal solid waste (biogenic)",
                ),
                (
                    "MSN",
                    "municipal_solid_nonbiogenic",
                    "short_tons",
                    9.0,
                    12.0,
                    "fossil",
                    "petroleum",
                    "solid",
                    "waste",
                    "Municipal solid waste (non-biogenic)",
                ),
                (
                    "MSW",
                    "municipal_solid_waste",
                    "short_tons",
                    9.0,
                    12.0,
                    "renewable",
                    "biomass",
                    "solid",
                    "waste",
                    "Municipal solid waste (all types)",
                ),
                (
                    "MWH",
                    "electricity_storage",
                    "mwh",
                    np.nan,
                    np.nan,
                    "other",
                    "other",
                    pd.NA,
                    "other",
                    "Electricity used for electricity storage",
                ),
                (
                    "NG",
                    "natural_gas",
                    "mcf",
                    0.8,
                    1.1,
                    "fossil",
                    "gas",
                    "gas",
                    "gas",
                    "Natural gas",
                ),
                (
                    "NUC",
                    "nuclear",
                    pd.NA,
                    np.nan,
                    np.nan,
                    "other",
                    "other",
                    pd.NA,
                    "nuclear",
                    "Nuclear, including uranium, plutonium, and thorium",
                ),
                (
                    "OBG",
                    "other_biomass_gas",
                    "mcf",
                    0.36,
                    1.6,
                    "renewable",
                    "biomass",
                    "gas",
                    "waste",
                    "Other biomass gas, including digester gas, methane, and other biomass gasses",
                ),
                (
                    "OBL",
                    "other_biomass_liquid",
                    "barrels",
                    3.5,
                    4.0,
                    "renewable",
                    "biomass",
                    "liquid",
                    "waste",
                    "Other biomass liquids",
                ),
                (
                    "OBS",
                    "other_biomass_solid",
                    "short_tons",
                    8.0,
                    25.0,
                    "renewable",
                    "biomass",
                    "solid",
                    "waste",
                    "Other biomass solids",
                ),
                (
                    "OG",
                    "other_gas",
                    "mcf",
                    0.32,
                    3.3,
                    "fossil",
                    "other",
                    "gas",
                    "gas",
                    "Other gas",
                ),
                (
                    "OTH",
                    "other",
                    pd.NA,
                    np.nan,
                    np.nan,
                    "other",
                    "other",
                    pd.NA,
                    "other",
                    "Other",
                ),
                (
                    "PC",
                    "petroleum_coke",
                    "short_tons",
                    24.0,
                    30.0,
                    "fossil",
                    "petroleum",
                    "solid",
                    "coal",
                    "Petroleum coke",
                ),
                (
                    "PG",
                    "propane_gas",
                    "mcf",
                    2.5,
                    2.75,
                    "fossil",
                    "petroleum",
                    "gas",
                    "gas",
                    "Gaseous propane",
                ),
                (
                    "PUR",
                    "purchased_steam",
                    pd.NA,
                    np.nan,
                    np.nan,
                    "other",
                    "other",
                    pd.NA,
                    "other",
                    "Purchased steam",
                ),
                (
                    "RC",
                    "refined_coal",
                    "short_tons",
                    20.0,
                    29.0,
                    "fossil",
                    "coal",
                    "solid",
                    "coal",
                    "Refined coal",
                ),
                (
                    "RFO",
                    "residual_fuel_oil",
                    "barrels",
                    5.7,
                    6.9,
                    "fossil",
                    "petroleum",
                    "liquid",
                    "oil",
                    "Residual fuel oil, including Nos. 5 & 6 fuel oils and bunker C fuel oil",
                ),
                (
                    "SC",
                    "coal_synfuel",
                    "short_tons",
                    np.nan,
                    np.nan,
                    "fossil",
                    "coal",
                    "solid",
                    "coal",
                    "Coal synfuel. Coal-based solid fuel that has been processed by a coal synfuel plant, and coal-based fuels such as briquettes, pellets, or extrusions, which are formed from fresh or recycled coal and binding materials.",
                ),
                (
                    "SG",
                    "syngas_other",
                    "mcf",
                    np.nan,
                    np.nan,
                    "fossil",
                    "other",
                    "gas",
                    "gas",
                    "Synthetic gas, other than coal-derived",
                ),
                (
                    "SGC",
                    "syngas_coal",
                    "mcf",
                    0.2,
                    0.3,
                    "fossil",
                    "coal",
                    "gas",
                    "gas",
                    "Coal-derived synthesis gas",
                ),
                (
                    "SGP",
                    "syngas_petroleum_coke",
                    "mcf",
                    0.2,
                    1.1,
                    "fossil",
                    "petroleum",
                    "gas",
                    "gas",
                    "Synthesis gas from petroleum coke",
                ),
                (
                    "SLW",
                    "sludge_waste",
                    "short_tons",
                    10.0,
                    16.0,
                    "renewable",
                    "biomass",
                    "liquid",
                    "waste",
                    "Sludge waste",
                ),
                (
                    "SUB",
                    "subbituminous_coal",
                    "short_tons",
                    15.0,
                    20.0,
                    "fossil",
                    "coal",
                    "solid",
                    "coal",
                    "Sub-bituminous coal",
                ),
                (
                    "SUN",
                    "solar",
                    pd.NA,
                    np.nan,
                    np.nan,
                    "renewable",
                    "other",
                    pd.NA,
                    "solar",
                    "Solar",
                ),
                (
                    "TDF",
                    "tire_derived_fuels",
                    "short_tons",
                    16.0,
                    32.0,
                    "other",
                    "other",
                    "solid",
                    "waste",
                    "Tire-derived fuels",
                ),
                (
                    "WAT",
                    "water",
                    pd.NA,
                    np.nan,
                    np.nan,
                    "renewable",
                    "other",
                    pd.NA,
                    "hydro",
                    "Water at a conventional hydroelectric turbine, and water used in wave buoy hydrokinetic technology, current hydrokinetic technology, and tidal hydrokinetic technology, or pumping energy for reversible (pumped storage) hydroelectric turbine",
                ),
                (
                    "WC",
                    "waste_coal",
                    "short_tons",
                    6.5,
                    16.0,
                    "fossil",
                    "coal",
                    "solid",
                    "coal",
                    "Waste/Other coal, including anthracite culm, bituminous gob, fine coal, lignite waste, waste coal.",
                ),
                (
                    "WDL",
                    "wood_liquids",
                    "barrels",
                    8.0,
                    14.0,
                    "renewable",
                    "biomass",
                    "liquid",
                    "waste",
                    "Wood waste liquids excluding black liquor, including red liquor, sludge wood, spent sulfite liquor, and other wood-based liquids",
                ),
                (
                    "WDS",
                    "wood_solids",
                    "short_tons",
                    7.0,
                    18.0,
                    "renewable",
                    "biomass",
                    "solid",
                    "waste",
                    "Wood/Wood waste solids, including paper pellets, railroad ties, utility poles, wood chips, park, and wood waste solids",
                ),
                (
                    "WH",
                    "waste_heat",
                    pd.NA,
                    np.nan,
                    np.nan,
                    "other",
                    "other",
                    pd.NA,
                    "other",
                    "Waste heat not directly attributed to a fuel source. WH should only be reported when the fuel source is undetermined, and for combined cycle steam turbines that do not have supplemental firing.",
                ),
                (
                    "WND",
                    "wind",
                    pd.NA,
                    np.nan,
                    np.nan,
                    "renewable",
                    "other",
                    pd.NA,
                    "wind",
                    "Wind",
                ),
                (
                    "WO",
                    "waste_oil",
                    "barrels",
                    3.0,
                    5.8,
                    "fossil",
                    "petroleum",
                    "liquid",
                    "oil",
                    "Waste/Other oil, including crude oil, liquid butane, liquid propane, naptha, oil waste, re-refined motor oil, sludge oil, tar oil, or other petroleum-based liquid wastes",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {
            "BL": "BLQ",
            "HPS": "WAT",
            "ng": "NG",
            "WOC": "WC",
            "OW": "WO",
            "WT": "WND",
            "H2": "OG",
            "OOG": "OG",
            "Sun": "SUN",
            "sub": "SUB",
            "PV": "SUN",  # Plant ID 59898 and 59899 in 2024 ER
        },
        "ignored_codes": [
            0,
            "0",
            "OO",
            "BM",
            "CBL",
            "COL",
            "N",
            "no",
            "PL",
            "ST",
        ],
    },
    "core_eia__codes_fuel_transportation_modes": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "GL",
                    "great_lakes",
                    "Shipments of coal moved to consumers via the Great Lakes. These shipments are moved via the Great Lakes coal loading docks.",
                ),
                (
                    "OP",
                    "onsite_production",
                    "Fuel is produced on-site, making fuel shipment unnecessary.",
                ),
                (
                    "RR",
                    "rail",
                    "Shipments of fuel moved to consumers by rail (private or public/commercial). Included is coal hauled to or away from a railroad siding by truck if the truck did not use public roads.",
                ),
                (
                    "RV",
                    "river",
                    "Shipments of fuel moved to consumers via river by barge.  Not included are shipments to Great Lakes coal loading docks, tidewater piers, or coastal ports.",
                ),
                ("PL", "pipeline", "Shipments of fuel moved to consumers by pipeline"),
                (
                    "SP",
                    "slurry_pipeline",
                    "Shipments of coal moved to consumers by slurry pipeline.",
                ),
                (
                    "TC",
                    "tramway_conveyor",
                    "Shipments of fuel moved to consumers by tramway or conveyor.",
                ),
                (
                    "TP",
                    "tidewater_port",
                    "Shipments of coal moved to Tidewater Piers and Coastal Ports for further shipments to consumers via coastal water or ocean.",
                ),
                (
                    "TR",
                    "truck",
                    "Shipments of fuel moved to consumers by truck.  Not included is fuel hauled to or away from a railroad siding by truck on non-public roads.",
                ),
                (
                    "WT",
                    "other_waterway",
                    "Shipments of fuel moved to consumers by other waterways.",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {
            "TK": "TR",
            "tk": "TR",
            "tr": "TR",
            "WA": "WT",
            "wa": "WT",
            "CV": "TC",
            "cv": "TC",
            "rr": "RR",
            "pl": "PL",
            "rv": "RV",
            "RT": "TR",  # This is based on a guess. No definitive proof. Culprit is plant_id_eia 3935 in October 2024 in the coalmine table.
        },
        "ignored_codes": ["UN"],
    },
    "core_eia__codes_fuel_types_agg": {
        "df": pd.DataFrame(
            columns=["code", "description"],
            data=[
                ("SUN", "Solar PV and thermal"),
                ("COL", "Coal"),
                ("DFO", "Distillate Petroleum"),
                ("GEO", "Geothermal"),
                ("HPS", "Hydroelectric Pumped Storage"),
                ("HYC", "Hydroelectric Conventional"),
                ("MLG", "Biogenic Municipal Solid Waste and Landfill Gas"),
                ("NG", "Natural Gas"),
                ("NUC", "Nuclear"),
                ("OOG", "Other Gases"),
                ("ORW", "Other Renewables"),
                ("OTH", "Other (including Nonbiogenic Municipal Solid Waste)"),
                ("PC", "Petroleum Coke"),
                ("RFO", "Residual Petroleum"),
                ("WND", "Wind"),
                ("WOC", "Waste Coal"),
                ("WOO", "Waste Oil"),
                ("WWW", "Wood and Wood Waste"),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_eia__codes_contract_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "C",
                    "contract",
                    "Fuel received under a purchase order or contract with a term of one year or longer.  Contracts with a shorter term are considered spot purchases ",
                ),
                (
                    "NC",
                    "new_contract",
                    "Fuel received under a purchase order or contract with duration of one year or longer, under which deliveries were first made during the reporting month",
                ),
                ("S", "spot_purchase", "Fuel obtained through a spot market purchase"),
                (
                    "T",
                    "tolling_agreement",
                    "Fuel received under a tolling agreement (bartering arrangement of fuel for generation)",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {"N": "NC"},
        "ignored_codes": [],
    },
    "core_eia__codes_prime_movers": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("BA", "battery_storage", "Energy Storage, Battery"),
                (
                    "BT",
                    "binary_cycle_turbine",
                    "Turbines Used in a Binary Cycle. Including those used for geothermal applications",
                ),
                (
                    "CA",
                    "combined_cycle_steam_turbine",
                    "Combined-Cycle, Steam Turbine Part",
                ),
                ("CC", "combined_cycle_total", "Combined-Cycle, Total Unit"),
                ("CE", "compressed_air_storage", "Energy Storage, Compressed Air"),
                (
                    "CP",
                    "concentrated_solar_storage",
                    "Energy Storage, Concentrated Solar Power",
                ),
                (
                    "CS",
                    "combined_cycle_single_shaft",
                    "Combined-Cycle Single-Shaft Combustion Turbine and Steam Turbine share of single",
                ),
                (
                    "CT",
                    "combined_cycle_combustion_turbine",
                    "Combined-Cycle Combustion Turbine Part",
                ),
                (
                    "ES",
                    "other_storage",
                    "Energy Storage, Other (Specify on Schedule 9, Comments)",
                ),
                ("FC", "fuel_cell", "Fuel Cell"),
                ("FW", "flywheel_storage", "Energy Storage, Flywheel"),
                (
                    "GT",
                    "gas_combustion_turbine",
                    "Combustion (Gas) Turbine. Including Jet Engine design",
                ),
                ("HA", "hydrokinetic_axial_flow", "Hydrokinetic, Axial Flow Turbine"),
                ("HB", "hydrokinetic_wave_buoy", "Hydrokinetic, Wave Buoy"),
                ("HK", "hydrokinetic_other", "Hydrokinetic, Other"),
                (
                    "HY",
                    "hydraulic_turbine",
                    "Hydraulic Turbine. Including turbines associated with delivery of water by pipeline.",
                ),
                (
                    "IC",
                    "internal_combustion",
                    "Internal Combustion (diesel, piston, reciprocating) Engine",
                ),
                ("OT", "other", "Other"),
                (
                    "PS",
                    "pumped_storage",
                    "Energy Storage, Reversible Hydraulic Turbine (Pumped Storage)",
                ),
                ("PV", "solar_pv", "Solar Photovoltaic"),
                (
                    "ST",
                    "steam_turbine",
                    "Steam Turbine. Including Nuclear, Geothermal, and Solar Steam (does not include Combined Cycle).",
                ),
                ("UNK", "unknown", "Unknown prime mover."),
                ("WS", "wind_offshore", "Wind Turbine, Offshore"),
                ("WT", "wind_onshore", "Wind Turbine, Onshore"),
            ],
        ).convert_dtypes(),
        "code_fixes": {
            "ic": "IC",
            # There is literally one 'ic' from 2002.
            "WY": "WT",
        },  # The WY shows up once in plant_id_eia 65738 in 2023. Other years are WT.
        "ignored_codes": [],
    },
    "core_eia__codes_sector_consolidated": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (1, "electric_utility", "Traditional regulated electric utilities."),
                (
                    2,
                    "ipp_non_cogen",
                    "Independent power producers which are not cogenerators.",
                ),
                (
                    3,
                    "ipp_cogen",
                    "Independent power producers which are cogenerators, but whose primary business purpose is the same of electricity to the public.",
                ),
                (
                    4,
                    "commercial_non_cogen",
                    "Commercial non-cogeneration facilities that produce electric power, are connected to the grid, and can sell power to the public.",
                ),
                (
                    5,
                    "commercial_cogen",
                    "Commercial cogeneration facilities that produce electric power, are connected to the grid, and can sell power to the public.",
                ),
                (
                    6,
                    "industrial_non_cogen",
                    "Industrial non-cogeneration facilities that produce electric power, are connected to the grid, and can sell power to the public.",
                ),
                (
                    7,
                    "industrial_cogen",
                    "Industrial cogeneration facilities that produce electric power, are connected to the grid, and can sell power to the public",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_eia__codes_steam_plant_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    1,
                    "steam_over_100mw",
                    "Plants with combustible-fueled steam-electric generators with a sum of 100 MW or more steam-electric nameplate capacity (including combined cycle steam-electric generators with duct firing).",
                ),
                (
                    2,
                    "steam_between_10mw_and_100mw",
                    "Plants with combustible-fueled steam-electric generators with a sum of 10 MW or more but less than 100 MW steam-electric nameplate capacity (including combined cycle steam-electric generators with duct firing).",
                ),
                (
                    3,
                    "nuclear_over_100mw",
                    "Plants with nuclear fueled generators, combined cycle steam-electric generators without duct firing and solar thermal electric generators using a steam cycle with a sum of 100 MW or more steam-electric nameplate capacity.",
                ),
                (
                    4,
                    "non_steam",
                    "Plants with non-steam fueled electric generators (wind, PV, geothermal, fuel cell, combustion turbines, IC engines, etc.) and electric generators not meeting conditions of categories above.",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_eia__codes_reporting_frequencies": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "A",
                    "annual",
                    "The respondent only provides an annual total(s) for this record via the EIA-923 annual survey form.  Any monthly data in this record is estimated based on the respondent's reported annual total(s) and power plants with similar characteristics to this plant.",
                ),
                (
                    "M",
                    "monthly",
                    "The respondent provides monthly values for this record and does so via the EIA-923 monthly survey form.",
                ),
                (
                    "AM",
                    "monthly_annual",
                    "The respondent provides monthly values for this record, but does so once per year via the EIA-923 annual survey form.",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_pudl__codes_data_maturities": {
        "df": pd.DataFrame(
            columns=["code", "description"],
            data=[
                (
                    "final",
                    "Data that has been reviewed and validated by the publishing agency, and is considered to be in its final form. Note that even final data is subject to later revision, sometimes years after the fact.",
                ),
                (
                    "provisional",
                    "An early draft of final release data, that has not yet been fully reviewed or validated by the publishing agency. Should be used with caution. E.g. Early Release versions of the complete annual EIA-860 and EIA-923 data.",
                ),
                (
                    "monthly_update",
                    "Data that is updated monthly throughout the year, but that is not monthly in resolution. Should be used with caution, as it may be revised when incorporated into final annual reporting. E.g. the generator attributes reported in the EIA-860m.",
                ),
                (
                    "incremental_ytd",
                    "Incremental releases of data with sub-annual resolution. Should be used with caution, as in many cases not all respondents are required to report at sub-annual frequency, meaning data coverage may not be complete. This data is also likely to be revised prior to its final annual release. E.g. the EIA-923 monthly or FERC Form 1 quarterly data releases.",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_eia__codes_balancing_authorities": {
        "df": pd.read_csv(
            StringIO(
                """code,label,description,report_timezone,balancing_authority_region_name_eia,balancing_authority_retirement_date,balancing_authority_region_code_eia,interconnect_code_eia,is_generation_only
AEC,power_south_coop,PowerSouth Energy Cooperative,America/Chicago,Southeast,2021-09-01,SE,eastern,False
AESO,alberta_electric_system_operator,Alberta Electric System Operator,,Canada,,CAN,,False
AECI,associated_electric_coop,"Associated Electric Cooperative, Inc.",America/Chicago,Midwest,,MIDW,eastern,False
AVA,avista,Avista Corporation,America/Los_Angeles,Northwest,,NW,western,False
AVRN,avangrid,Avangrid Renewables LLC,America/Los_Angeles,Northwest,,NW,,True
AZPS,arizona_public_service,Arizona Public Service Company,America/Phoenix,Southwest,,SW,western,False
BANC,northern_california,Balancing Authority of Northern California,America/Los_Angeles,California,,CAL,western,False
BCHA,bc_hydro,British Columbia Hydro and Power Authority,,Canada,,CAN,,False
BPAT,bonneville_power,Bonneville Power Administration,America/Los_Angeles,Northwest,,NW,western,False
CHPD,public_utility_district_of_chelan_county,Public Utility District No. 1 of Chelan County,America/Los_Angeles,Northwest,,NW,western,False
CISO,california_iso,California Independent System Operator,America/Los_Angeles,California,,CAL,western,False
CEA,chugach_electric,Chugach Electric Assn Inc,Anchorage,,,,,
CEN,centro_nacional_de_control_de_energia,Centro Nacional de Control de Energia,,Mexico,,MEX,,False
CFE,comision_federal_de_electricidad,Comisión Federal de Electricidad,,Mexico,2018-07-01,MEX,,False
CPLE,duke_energy_progress_east,Duke Energy Progress East,America/New_York,Carolinas,,CAR,eastern,False
CPLW,duke_energy_progress_west,Duke Energy Progress West,America/New_York,Carolinas,,CAR,eastern,False
CSTO,constellation,"Constellation Energy Control and Dispatch, LLC",,,,,,False
CSWS,public_service_company_of_oklahoma_and_southwestern_electric,American Electric Power Service Corp. As Agent For Public Svc. Co. Of Oklahoma & SW Ele Pwr Co.,,,,,,False
DEAA,arlington_valley,"Arlington Valley, LLC - AVBA",America/Phoenix,Southwest,,SW,western,True
DOPD,public_utility_of_douglas_county,PUD No. 1 of Douglas County,America/Los_Angeles,Northwest,,NW,western,False
DUK,duke_energy_carolinas,Duke Energy Carolinas,America/New_York,Carolinas,,CAR,eastern,False
EDE,empire_district,The Empire District Electric Company,,,,,,False
EEI,electric_energy,"Electric Energy, Inc.",America/Chicago,Midwest,2020-02-29,MIDW,eastern,False
EPE,el_paso_electric,El Paso Electric Company,America/Phoenix,Southwest,,SW,western,False
ERCO,electric_reliability_council_of_texas,"Electric Reliability Council of Texas, Inc.",America/Chicago,Texas,,TEX,ercot,False
FMPP,florida_municipal_power_pool,Florida Municipal Power Pool,America/New_York,Florida,,FLA,eastern,False
FPC,progress_energy_florida,Progress Energy Florida,America/New_York,Florida,,FLA,eastern,False
FPL,florida_power_and_light,Florida Power & Light Company,America/New_York,Florida,,FLA,eastern,False
GCPD,public_utility_grant_county,"Public Utility District No. 2 of Grant County, Washington",America/Los_Angeles,Northwest,,NW,western,False
GLHB,gridliance,GridLiance (GLHB),America/Chicago,Midwest,2022-09-01,MIDW,,True
GRDA,grand_river_dam,Grand River Dam Authority,,,,,,False
GRID,gridforce_energy_management,"Gridforce Energy Management, LLC",America/Los_Angeles,Pacific Northwest,,,western,True
GRIF,griffith_energy,"Griffith Energy, LLC",America/Phoenix,Southwest,2023-11-01,SW,western,True
GRIS,gridforce_south,Gridforce South,,,,,,False
GRMA,gila_river_power,"Gila River Power, LLC",America/Phoenix,Southwest,2018-05-03,SW,western,True
GVL,gainesville_regional,Gainesville Regional Utilities,America/New_York,Florida,,FLA,eastern,False
GWA,naturener_power_watch,"NaturEner Power Watch, LLC (GWA)",America/Denver,Northwest,,NW,western,True
HECO,hawaiian_electric,Hawaiian Electric Co Inc,,,,,,False
HGMA,new_harquahala,"New Harquahala Generating Company, LLC - HGBA",America/Phoenix,Southwest,,SW,western,True
HQT,hydro_quebec,Hydro-Québec TransEnergie,,Canada,,CAN,,False
HST,city_of_homestead,City of Homestead,America/New_York,Florida,,FLA,eastern,False
IESO,ontario_ieso,Ontario Independent Electric System Operator,,Canada,,CAN,,False
IID,imperial_irrigation,Imperial Irrigation District,America/Los_Angeles,California,,CAL,western,False
INDN,independence_power_and_light,"Independence Power & Light (Independence,Missouri)",,,,,,False
IPCO,idaho_power,Idaho Power Company,America/Los_Angeles,Northwest,,NW,western,False
ISNE,iso_new_england,ISO New England Inc.,America/New_York,New England,,NE,eastern,False
JEA,jacksonville_energy,Jacksonville Energy,America/New_York,Florida,,FLA,eastern,False
KACY,kansas_city,Board Of Public Utilities (Kansas City KS),,,,,,False
KCPL,kansas_city_power_and_light,Kansas City Power & Light Company,,,,,,False
LDWP,los_angeles_dept_of_water_and_power,Los Angeles Department of Water and Power,America/Los_Angeles,California,,CAL,western,False
LES,lincoln_electric,Lincoln Electric System,,,,,,False
LGEE,louisville_gas_and_electric_and_kentucky,LG&E and KU Services Company as agent for Louisville Gas and Electric Company and Kentucky Utilities,America/New_York,Midwest,,MIDW,eastern,False
MHEB,manitoba_hydro,Manitoba Hydro,,Canada,,CAN,,False
MISO,midcontinent_iso,"Midcontinent Independent Transmission System Operator, Inc..",America/New_York,Midwest,,MIDW,eastern,False
MPS,kansas_city_power_and_light_missouri,KCPL - Greater Missouri Operations,,,,,,False
NBSO,new_brunswick_system_operator,New Brunswick System Operator,,Canada,,CAN,,False
NEVP,nevada_power,Nevada Power Company,America/Los_Angeles,Northwest,,NW,western,False
NPPD,nebraska_public_power,Nebraska Public Power District,,,,,,False
NSB,new_smyrna_beach,"New Smyrna Beach, Utilities Commission of",America/New_York,Florida,2020-01-08,FLA,eastern,False
NWMT,northwestern_energy,NorthWestern Energy (NWMT),America/Denver,Northwest,,NW,western,False
NYIS,new_york_iso,New York Independent System Operator,America/New_York,New York,,NY,eastern,False
OKGE,oklahoma_gas_and_electric,Oklahoma Gas And Electric Co.,,,,,,False
OPPD,omaha_public_power,Omaha Public Power District,,,,,,False
OVEC,ohio_valley,Ohio Valley Electric Corporation,America/New_York,Mid-Atlantic,2018-12-01,MIDA,eastern,False
PACE,pacificorp_east,PacifiCorp - East,America/Denver,Northwest,,NW,western,False
PACW,pacificorp_west,PacifiCorp - West,America/Los_Angeles,Northwest,,NW,western,False
PGE,portland_general_electric,Portland General Electric Company,America/Los_Angeles,Northwest,,NW,western,False
PJM,pjm_interconnection,"PJM Interconnection, LLC",America/New_York,Mid-Atlantic,,MIDA,eastern,False
PNM,public_service_company_of_new_mexico,Public Service Company of New Mexico,America/Phoenix,Southwest,,SW,western,False
PSCO,public_service_company_of_colorado,Public Service Company of Colorado,America/Denver,Northwest,,NW,western,False
PSEI,pugent_sound_energy,Puget Sound Energy,America/Los_Angeles,Northwest,,NW,western,False
SC,south_carolina_public_service,South Carolina Public Service Authority,America/New_York,Carolinas,,CAR,eastern,False
SCEG,south_carolina_electric_and_gas,South Carolina Electric & Gas Company,America/New_York,Carolinas,,CAR,eastern,False
SCL,seattle_city_light,Seattle City Light,America/Los_Angeles,Northwest,,NW,western,False
SEC,seminole_electric_coop,Seminole Electric Cooperative,America/New_York,Florida,,FLA,eastern,False
SECI,sunflower_electric_power,Sunflower Electric Power Corporation,,,,,,False
SEPA,southeastern_power,Southeastern Power Administration,America/Chicago,Southeast,,SE,eastern,True
SOCO,southern_company_services,"Southern Company Services, Inc. - Trans",America/Chicago,Southeast,,SE,eastern,False
SPA,southwestern_power,Southwestern Power Administration,America/Chicago,Central,,CENT,eastern,False
SPC,saskatchewan_power_corporation,Saskatchewan Power Corporation,,Canada,,CAN,,False
SPRM,city_utilities_of_springfield,"City Utilities Of Springfield, MO",,,,,,False
SPS,southwestern_public_service,Southwestern Public Service Co. (Xcel Energy),,,,,,False
SRP,salt_river_project,Salt River Project,America/Phoenix,Southwest,,SW,western,False
SWPP,southwest_power_pool,Southwest Power Pool,America/Chicago,Central,,CENT,eastern,False
TAL,city_of_tallahassee,City of Tallahassee,America/New_York,Florida,,FLA,eastern,False
TEC,tampa_electric,Tampa Electric Company,America/New_York,Florida,,FLA,eastern,False
TEPC,tuscon_electric_power,Tucson Electric Power Company,America/Phoenix,Southwest,,SW,western,False
TIDC,turlock_irrigation_district,Turlock Irrigation District,America/Los_Angeles,California,,CAL,western,False
TPWR,city_of_tacoma,"City of Tacoma, Department of Public Utilities, Light Division",America/Los_Angeles,Northwest,,NW,western,False
TVA,tennessee_valley_authority,Tennessee Valley Authority,America/Chicago,Tennessee,,TEN,eastern,False
WACM,western_area_power_mountain,Western Area Power Administration - Rocky Mountain Region,America/Phoenix,Northwest,,NW,western,False
WALC,western_area_power_southwest,Western Area Power Administration - Desert Southwest Region,America/Phoenix,Southwest,,SW,western,False
WAUE,western_area_power_east,Western Area Power Administration - Upper Great Plains East,,,,,,False
WAUW,western_area_power_west,Western Area Power Administration UGP West,America/Denver,Northwest,,NW,western,False
WFEC,western_farmers_electric_coop,Western Farmers Electric Cooperative,,,,,,False
WR,westar_energy,Westar Energy,,,,,,False
WWA,naturener_wind,"NaturEner Wind Watch, LLC",America/Denver,Northwest,,NW,western,True
YAD,alcoa_power_yadkin,"Alcoa Power Generating, Inc. - Yadkin Division",America/New_York,Carolinas,,CAR,eastern,True""",
            ),
            parse_dates=["balancing_authority_retirement_date"],
        ).convert_dtypes(),
        "code_fixes": {
            "CA": "CISO",
            "CI": "CISO",
            # "CP" is associated with plants identified as CPLE elsewhere / later.
            # with the exception of plant 61527 which is later correctly identified as
            # DUK.
            "CP": "CPLE",
            "DU": "DUK",
            "EP": "EPE",  # El Paso Electric
            "ER": "ERCO",  # ERCOT, Texas
            "IP": "IPCO",  # Idaho Power Company
            "IS": "ISNE",
            "MI": "MISO",
            "NE": "NEVP",
            "NVE": "NEVP",
            "NY": "NYIS",
            # "PA" is manually remapped such that in OR -> PACW and UT -> PACE
            "PJ": "PJM",
            "PS": "PSCO",
            # The plants with BA code SE are all later and elsewhere associated with the
            # Seminole Electric Co-op, SEC
            "SE": "SEC",
            "SR": "SRP",  # Salt River Project
            # All plants associated with SW are later and elsewhere associated with
            # SWPP, Southwest Power Pool. Some transition to ERCO (ERCOT) in later years
            # but they are correctly labeled in those years.
            "SW": "SWPP",
            "TEN": "TVA",
            "TEX": "ERCO",
            "TIC": "TIDC",
            "TID": "TIDC",
        },
        "ignored_codes": [],
    },
    "core_eia__codes_regulations": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "FD",
                    "federal",
                    "The most stringent applicable statute or regulation determining the pollutant's control standards for this boiler is federal.",
                ),
                (
                    "ST",
                    "state",
                    "The most stringent applicable statute or regulation determining the pollutant's control standards for this boiler is state-level.",
                ),
                (
                    "LO",
                    "local",
                    "The most stringent applicable statute or regulation determining the pollutant's control standards for this boiler is local.",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {"St": "ST"},
        "ignored_codes": ["NA", "XX"],
    },
    "core_eia__codes_so2_compliance_strategies": {  # TO DO: harmonize these columns with envr equip data when integrated.
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("BO", "out_of_service", "Burner out of service."),
                ("CF", "fluidized_bed_combustor", "Fluidized bed combustor."),
                ("CU", "control_unit", "Control unit under Phase I extension plan."),
                ("FR", "flue_gas_recirculation", "Flue gas recirculation."),
                (
                    "IF",
                    "flue_gas_desulfurization",
                    "Use flue gas desulfurization unit or other SO2 control process (specify the specific type of equipment in Schedule 6A).",
                ),
                ("LA", "low_excess_air", "Low excess air."),
                ("LN", "low_nitrogen_oxide_burner", "Low nitrogen oxide burner."),
                ("MS", "meeting_standard", "Currently meeting standard."),
                ("RP", "repower_unit", "Repower unit."),
                ("SS", "lower_sulfur_fuel", "Switch to lower sulfur fuel."),
                (
                    "SU",
                    "substitution_unit",
                    "Designate Phase II unit(s) as substitution unit(s).",
                ),
                ("TU", "transfer_unit", "Transfer unit under Phase I extension plan."),
                (
                    "UC",
                    "compensating_units",
                    "Decrease utilization - designate Phase II unit(s) as compensating unit(s).",
                ),
                (
                    "UE",
                    "conservation_efficiency",
                    "Decrease utilization - rely on energy conservation and/or improved efficiency.",
                ),
                (
                    "US",
                    "sulfur_free_generators",
                    "Decrease utilization - designate sulfur-free generators to compensate.",
                ),
                ("UP", "purchase_power", "Decrease utilization - purchase power."),
                ("WA", "allowances", "Allocated allowances and purchase allowances."),
                ("OT", "other", "Other: specify in schedule 7."),
                ("OV", "overfire_air", "Overfire air."),
                (
                    "SE",
                    "seeking_revision",
                    "Seeking revision of government regulation.",
                ),
                ("ND", "not_determined", "Not determined at this time."),
                ("NP", "no_plans", "No plans to control."),
            ],
        ).convert_dtypes(),
        "code_fixes": {"NC": "NP"},
        "ignored_codes": ["NA", "DB"],
    },
    "core_eia__codes_so2_units": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "DC",
                    "ambient_air_quality",
                    "Ambient air quality concentration of sulfur dioxide (parts per million).",
                ),
                ("DH", "lbs_per_hour", "Pounds of sulfur dioxide emitted per hour."),
                (
                    "DL",
                    "declining_level",
                    "Annual sulfur dioxide emission level less than a level in a previous year.",
                ),
                (
                    "DM",
                    "stack_gas_ppm",
                    "Parts per million of sulfur dioxide in stack gas.",
                ),
                (
                    "DP",
                    "lbs_dioxide_per_mmbtu_fuel",
                    "Pounds of sulfur dioxide per million Btu in fuel.",
                ),
                (
                    "SB",
                    "lbs_sulfur_per_mmbtu_fuel",
                    "Pounds of sulfur per million Btu in fuel.",
                ),
                (
                    "SR",
                    "pct_efficiency",
                    "Percent sulfur removal efficiency (by weight).",
                ),
                ("SU", "pct_content", "Percent sulfur content of fuel (by weight)."),
                ("OT", "other", "Other: specify in schedule 7."),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_eia__codes_mercury_compliance_strategies": {  # TO DO: harmonize with 2021 data and equip data (most cols here should move to equip table.)
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "BH",
                    "baghouse",
                    "Baghouse (fabric filter). After 2011, values use more specific columns BS, BP, BR.",
                ),
                (
                    "BS",
                    "baghouse_shake_deflate",
                    "Baghouse (fabric filter), shake and deflate.",
                ),
                ("BP", "baghouse_pulse", "Baghouse (fabric filter), pulse."),
                (
                    "BR",
                    "baghouse_reverse_air",
                    "Baghouse (fabric filter), reverse air.",
                ),
                ("CD", "circulating_dry_scrubber", "Circulating dry scrubber."),
                (
                    "SD",
                    "spray_dryer",
                    "Spray dryer type / dry FGD / semi-dry FGD.",
                ),
                (
                    "DS",
                    "dry_scrubber",
                    "Dry scrubber. Generic categorical column from pre-2013 data.",
                ),
                (
                    "WS",
                    "wet_scrubber",
                    "Wet scrubber. Generic categorical column from pre-2013 data.",
                ),
                (
                    "DSI",
                    "dry_sorbent_injector",
                    "Dry sorbent (powder) injection type.",
                ),
                (
                    "ACI",
                    "activated_carbon_injection",
                    "Activated carbon injection system.",
                ),
                (
                    "LIJ",
                    "lime_injection",
                    "Lime injection.",
                ),
                (
                    "EP",
                    "electrostatic_precipitator",
                    "Electrostatic precipitator. After 2011, values use more specific columns EC, EH, EK, EW.",
                ),
                (
                    "EC",
                    "ec_cold_side_w_fg_cond",
                    "Electrostatic precipitator, cold side, with flue gas conditioning.",
                ),
                (
                    "EH",
                    "ec_hot_side_w_fg_cond",
                    "Electrostatic precipitator, hot side, with flue gas conditioning.",
                ),
                (
                    "EK",
                    "ec_cold_side_wo_fg_cond",
                    "Electrostatic precipitator, cold side, without flue gas conditioning.",
                ),
                (
                    "EW",
                    "ec_hot_side_wo_fg_cond",
                    "Electrostatic precipitator, hot side, without flue gas conditioning.",
                ),
                (
                    "FGD",
                    "flue_gas_desulfurization",
                    "Flue gas desulfurization (pre-2013 only.)",
                ),
                ("JB", "jet_bubbling_reactor", "Jet bubbling reactor (wet) scrubber."),
                (
                    "MA",
                    "mechanically_aided_scrubber",
                    "Mechanically aided type (wet) scrubber.",
                ),
                (
                    "PA",
                    "packed_type_scrubber",
                    "Packed type (wet) scrubber.",
                ),
                (
                    "SP",
                    "spray_type_scrubber",
                    "Spray type (wet) scrubber.",
                ),
                ("TR", "tray_type_scrubber", "Tray type (wet) scrubber."),
                ("VE", "venturi", "Venturi type (wet) scrubber."),
                ("OT", "other", "Other: specify in schedule 7."),
                ("ND", "not_determined", "Not determined at this time."),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": ["NA", "MC", "NP"],
    },
    "core_eia__codes_wet_dry_bottom": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "W",
                    "wet_bottom",
                    "A boiler with slag tanks that are installed at furnace throat to contain and remove molten ash from the furnace.",
                ),
                (
                    "D",
                    "dry_bottom",
                    "A boiler with no slag tanks at furnace throat area, where the throat area is clear, and bottom ash drops through the throat to the bottom ash water hoppers.",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_eia__codes_cooling_tower_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "MD",
                    "mechanical_dry",
                    "Mechanical draft, dry process",
                ),
                (
                    "MW",
                    "mechanical_wet",
                    "Mechanical draft, wet process",
                ),
                (
                    "ND",
                    "natural_dry",
                    "Natural draft, dry process",
                ),
                (
                    "NW",
                    "natural_wet",
                    "Natural draft, wet process",
                ),
                (
                    "WD",
                    "combo_wet_dry",
                    "Combination wet and dry process",
                ),
                (
                    "OT",
                    "other",
                    "Other",
                ),
            ],
        )
    },
    "core_eia__codes_cooling_water_sources": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "SW",
                    "surface_water",
                    "Surface Water (ex: river, canal, bay)",
                ),
                (
                    "GW",
                    "ground_water",
                    "Ground Water (ex: aquifer, well)",
                ),
                (
                    "PD",
                    "plant_discharge",
                    "Plant Discharge Water (ex: wastewater treatment plant discharge)",
                ),
                (
                    "OT",
                    "other",
                    "Other (specify in SCHEDULE 7)",
                ),
            ],
        )
    },
    "core_eia__codes_cooling_water_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "BR",
                    "brackish_water",
                    "Brackish water",
                ),
                (
                    "FR",
                    "fresh_water",
                    "Fresh water",
                ),
                (
                    "BE",
                    "reclaimed_water",
                    "Reclaimed water (ex: treated wastewater effluent)",
                ),
                (
                    "SA",
                    "saline_water",
                    "Saline water",
                ),
                ("OT", "other", "Other"),
            ],
        )
    },
    "core_eia__codes_cooling_system_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "DC",
                    "dry_cooling",
                    "Dry (air) cooling system",
                ),
                (
                    "H",
                    "hybrid_non_specified",
                    "Hybrid (non-specified)",
                ),
                (
                    "HRC",
                    "hybrid_wet_dry",
                    "Hybrid: cooling pond(s) or canal(s) with dry cooling",
                ),
                (
                    "HRF",
                    "hybrid_forced_draft_dry",
                    "Hybrid: forced draft cooling tower(s) with dry cooling",
                ),
                (
                    "HRI",
                    "hybrid_induced_draft_dry",
                    "Hybrid: induced draft cooling tower(s) with dry cooling",
                ),
                (
                    "O",
                    "once_through_non_specified",
                    "Once through (non-specified)",
                ),
                (
                    "O + R",
                    "once_through_non_specified_and_recirculating_non_specified",
                    "Once through (non-specified) and Recirculating (non-specified)",
                ),
                (
                    "OC",
                    "once_with_pond",
                    "Once through with cooling pond(s)",
                ),
                (
                    "OF",
                    "once_fresh",
                    "Once through, fresh water",
                ),
                (
                    "ON",
                    "once_without_pond",
                    "Once through without cooling pond(s)",
                ),
                (
                    "OS",
                    "once_saline",
                    "Once through, saline water",
                ),
                (
                    "R",
                    "recirculating_non_specified",
                    "Recirculating (non-specified)",
                ),
                (
                    "RC",
                    "recirculating_pond",
                    "Recirculating with cooling pond(s) or canal(s)",
                ),
                (
                    "RF",
                    "recirculating_forced_draft",
                    "Recirculating with forced draft cooling tower(s)",
                ),
                (
                    "RI",
                    "recirculating_induced_draft",
                    "Recirculating with induced draft cooling tower(s)",
                ),
                (
                    "RN",
                    "recirculating_natural_draft",
                    "Recirculating with natural draft cooling tower(s)",
                ),
                (
                    "HT",
                    "helper_tower",
                    "Helper tower",
                ),
                (
                    "OT",
                    "other",
                    "Other",
                ),
            ],
        ),
        "code_fixes": {
            "RECIRCULATING WITH INDUCED DRAFT COOLING TOWER": "RI",
            "DRY (AIR) COOLING SYSTEM": "DC",
            "ONCE THROUGH WITHOUT COOLING POND(S) OR CANAL(S)": "ON",
            "RECIRCULATING WITH COOLING PONDS": "RC",
            "RECIRCULATING": "R",
            "RECIRCULATING WITH NATURAL DRAFT COOLING TOWER": "RN",
            "ONCE THROUGH": "O",
            "ONCE THROUGH WITH COOLING PONDS": "OC",
            "HYBRID: RECIRCULATING WITH INDUCED DRAFT COOLING TOWER(S) WITH DRY COOLING": "HRI",
            "ONCE THROUGH AND RECIRCULATING": "O + R",
            "RECIRCULATING WITH FORCED DRAFT COOLING TOWER": "RF",
            "HYBRID (DRY AND WET COOLING)": "H",
            "OTHER - SPECIFY IN FOOTNOTE": "OT",
            "HYBRID: RECIRCULATING WITH FORCED DRAFT COOLING TOWER(S) WITH DRY COOLING": "HRF",
        },
        "ignored_codes": ["HR"],
    },
    "core_eia__codes_sorbent_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                (
                    "AF",
                    "alkaline_fly_ash",
                    "Alkaline fly ash",
                ),
                (
                    "AM",
                    "ammonia",
                    "Ammonia",
                ),
                (
                    "CC",
                    "calcium_carbide",
                    "Calcium carbide slurry",
                ),
                (
                    "CEF",
                    "ce_filtrate",
                    "CE filtrate",
                ),
                (
                    "CSH",
                    "caustic_sodium_hydroxide",
                    "Caustic sodium hydroxide",
                ),
                (
                    "DB",
                    "dibasic_acid_assisted",
                    "Dibasic acid assisted",
                ),
                (
                    "DL",
                    "dolomitic_limestone",
                    "Dolomitic limestone",
                ),
                (
                    "LA",
                    "lime_alkaline_fly_ash",
                    "Lime and alkaline fly ash",
                ),
                (
                    "LF",
                    "limestone_alkaline_fly_ash",
                    "Limestone and alkaline fly ash",
                ),
                (
                    "LI",
                    "lime_slacked_hydrated",
                    "Lime, slacked lime or hydrated lime",
                ),
                (
                    "LS",
                    "limestone",
                    "Limestone, dolomitic limestone or calcium carbonate",
                ),
                (
                    "MO",
                    "magnesium_oxide",
                    "Magnesium oxide",
                ),
                (
                    "OT",
                    "other",
                    "Other (specify in Schedule 7)",
                ),
                (
                    "SA",
                    "sodium_salt",
                    "Soda ash, sodium bicarbonate, sodium carbonate, sodium formate, or soda liquid",
                ),
                (
                    "SB",
                    "sodium_bicarbonate",
                    "Sodium bicarbonate",
                ),
                (
                    "SC",
                    "sodium_carbonate",
                    "Sodium carbonate",
                ),
                (
                    "SF",
                    "sodium_formate",
                    "Sodium formate",
                ),
                (
                    "SL",
                    "soda_liquid",
                    "Soda liquid",
                ),
                (
                    "SS",
                    "sodium_sulfite",
                    "Sodium sulfite",
                ),
                (
                    "TR",
                    "trona",
                    "Trona",
                ),
                (
                    "TW",
                    "treated_wastewater",
                    "Treated wastewater",
                ),
                (
                    "W",
                    "water",
                    "Water",
                ),
                (
                    "WT",
                    "water_or_treated_wastewater",
                    "Water or treated wastewater. Selected only if no other sorbent is used.",
                ),
            ],
        ),
        "code_fixes": {
            "CS": "CSH",
            "CE": "CEF",
        },
    },
    "core_eia__codes_wind_quality_class": {
        "df": pd.DataFrame(
            columns=[
                "code",
                "label",
                "description",
                "wind_speed_avg_ms",
                "extreme_fifty_year_gust_ms",
                "turbulence_intensity_a",
                "turbulence_intensity_b",
            ],
            data=[
                (1, "high_wind", "Class 1 - High Wind.", 10, 70, 0.21, 0.18),
                (2, "medium_wind", "Class 2 - Medium Wind.", 8.5, 59.6, 0.226, 0.191),
                (3, "low_wind", "Class 3 - Low Wind.", 7.5, 52.5, 0.240, 0.2),
                (4, "very_low_wind", "Class 4 - Very Low Wind.", 6, 42, 0.270, 0.22),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_eia__codes_storage_technology_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("ECC", "electro_chemical_capacitor", "Electro-chemical Capacitor"),
                ("FLB", "flow_battery", "Flow Battery"),
                ("LIB", "lithium_ion_battery", "Lithium-ion Battery"),
                ("MAB", "metal_air_battery", "Metal Air Battery"),
                ("NAB", "sodium_based_battery", "Sodium Based Battery"),
                ("NIB", "nickel_based_battery", "Nickel Based Battery"),
                ("OTH", "other", "Other"),
                ("PBB", "lead_acid_battery", "Lead-acid Battery"),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
    "core_eia__codes_storage_enclosure_types": {
        "df": pd.DataFrame(
            columns=["code", "label", "description"],
            data=[
                ("BL", "building", "Building"),
                ("CS", "containerized_stationary", "Containerized Stationary"),
                ("CT", "containerized_transportable", "Containerized Transportable"),
                ("OT", "other", "Other"),
            ],
        ).convert_dtypes(),
        "code_fixes": {},
        "ignored_codes": [],
    },
}

# The entity type codes were never fully reconciled. Preserving this work for reference.
# See https://github.com/catalyst-cooperative/pudl/issues/1392
DISABLED_CODE_METADATA = {
    "core_eia__codes_entity_types": {
        "df": pd.DataFrame(
            columns=[
                "code",
                "label",
                "description",
            ],
            data=[
                (
                    "A",
                    "municipal_marketing_authority",
                    "Municipal Marketing Authority. Voted into existence by the residents of a municipality and given authority for creation by the state government. They are nonprofit organizations",
                ),
                (
                    "B",
                    "behind_the_meter",
                    "Behind the Meter. Entities that install, own, and/or operate a system (usually photovoltaic), and sell, under a long term power purchase agreement (PPA) or lease, all the production from the system to the homeowner or business with which there is a net metering agreement. Third Party Owners (TPOs) of PV solar installations use this ownership code.",
                ),
                ("C", "cooperative", "Cooperative. Member-owned organizations."),
                ("COM", "commercial", "Commercial facility."),
                (
                    "D",
                    "nonutility_dsm_administrator",
                    "Non-utility DSM Administrator. Only involved with Demand-Side Management activities.",
                ),
                (
                    "F",
                    "federal",
                    "Federal. Government agencies with the authority to deliver energy to end-use customers.",
                ),
                ("G", "community_choice_aggregator", "Community Choice Aggregator."),
                (
                    "I",
                    "investor_owned",
                    "Investor-owned Utilities. Entities that are privately owned and provide a public service.",
                ),
                ("IND", "industrial", "Industrial facility."),
                (
                    "M",
                    "municipal",
                    "Municipal: Entities that are organized under authority of state statute to provide a public service to residents of that area.",
                ),
                ("O", "other", "Other entity type."),
                (
                    "P",
                    "political_subdivision",
                    'Political Subdivision. (also called "public utility district"): Independent of city or county government and voted into existence by a majority of the residents of any given area for the specific purpose of providing utility service to the voters. State laws provide for the formation of such districts.',
                ),
                ("PO", "power_marketer", "Power marketer."),
                ("PR", "private", "Private entity."),
                (
                    "Q",
                    "independent_power_producer",
                    "Independent Power Producer or Qualifying Facility. Entities that own power plants and sell their power into the wholesale market.",
                ),
                (
                    "R",
                    "retail_power_marketer",
                    "Retail Power Marketer or Energy Service Provider: Entities that market power to customers in restructured markets.",
                ),
                (
                    "S",
                    "state",
                    "State entities that own or operate facilities or provide a public service.",
                ),
                (
                    "T",
                    "transmission",
                    "Transmission: Entities that operate or own high voltage transmission wires that provide bulk power services.",
                ),
                ("U", "unknown", "Unknown entity type."),
                (
                    "W",
                    "wholesale_power_marketer",
                    "Wholesale Power Marketer: Entities that buy and sell power in the wholesale market.",
                ),
            ],
        ).convert_dtypes(),
        "code_fixes": {
            "Behind the Meter": "B",
            "Community Choice Aggregator": "G",
            "Cooperative": "C",
            "Facility": "Q",
            "Federal": "F",
            "Investor Owned": "I",
            "Municipal": "M",
            "Political Subdivision": "P",
            "Power Marketer": "PO",
            "Retail Power Marketer": "R",
            "State": "S",
            "Unregulated": "Q",
            "Wholesale Power Marketer": "W",
        },
        "ignored_codes": [],
    }
}
