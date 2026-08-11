"""Static seed data for AutoGraph.

Kept separate from seed.py (which does the writing) so the data itself
is easy to review, extend, or reuse in tests.
"""

MANUFACTURERS = [
    {"slug": "toyota", "name": "Toyota", "country": "Japan", "founded": 1937},
    {"slug": "bmw", "name": "BMW", "country": "Germany", "founded": 1916},
    {"slug": "nissan", "name": "Nissan", "country": "Japan", "founded": 1933},
    {"slug": "mazda", "name": "Mazda", "country": "Japan", "founded": 1920},
    {"slug": "honda", "name": "Honda", "country": "Japan", "founded": 1948},
    {"slug": "ford", "name": "Ford", "country": "USA", "founded": 1903},
    {"slug": "porsche", "name": "Porsche", "country": "Germany", "founded": 1931},
    {"slug": "audi", "name": "Audi", "country": "Germany", "founded": 1909},
    {"slug": "subaru", "name": "Subaru", "country": "Japan", "founded": 1953},
    {"slug": "chevrolet", "name": "Chevrolet", "country": "USA", "founded": 1911},
]

# family groups engines that share an architecture even when the specific
# tune/node differs - this is what powers the "shared engine family" queries.
ENGINES = [
    {"slug": "2jz-gte", "name": "2JZ-GTE", "family": "2JZ", "cylinders": "I6", "displacement": "3.0L", "aspiration": "Turbo", "horsepower": 320},
    {"slug": "b58b30", "name": "B58B30", "family": "B58", "cylinders": "I6", "displacement": "3.0L", "aspiration": "Turbo", "horsepower": 382},
    {"slug": "fa24", "name": "FA24", "family": "FA", "cylinders": "H4", "displacement": "2.4L", "aspiration": "Naturally Aspirated", "horsepower": 228},
    {"slug": "fa24dit", "name": "FA24DIT", "family": "FA", "cylinders": "H4", "displacement": "2.4L", "aspiration": "Turbo", "horsepower": 271},
    {"slug": "s58", "name": "S58", "family": "S58", "cylinders": "I6", "displacement": "3.0L", "aspiration": "Twin-Turbo", "horsepower": 473},
    {"slug": "vr38dett", "name": "VR38DETT", "family": "VR38", "cylinders": "V6", "displacement": "3.8L", "aspiration": "Twin-Turbo", "horsepower": 565},
    {"slug": "vq37vhr", "name": "VQ37VHR", "family": "VQ", "cylinders": "V6", "displacement": "3.7L", "aspiration": "Naturally Aspirated", "horsepower": 332},
    {"slug": "13b-rew", "name": "13B-REW", "family": "13B", "cylinders": "Rotary", "displacement": "1.3L", "aspiration": "Twin-Turbo", "horsepower": 255},
    {"slug": "13b-msp", "name": "13B-MSP Renesis", "family": "13B", "cylinders": "Rotary", "displacement": "1.3L", "aspiration": "Naturally Aspirated", "horsepower": 232},
    {"slug": "skyactiv-g25t", "name": "SkyActiv-G 2.5T", "family": "SkyActiv", "cylinders": "I4", "displacement": "2.5L", "aspiration": "Turbo", "horsepower": 250},
    {"slug": "k20c1", "name": "K20C1", "family": "K20", "cylinders": "I4", "displacement": "2.0L", "aspiration": "Turbo", "horsepower": 315},
    {"slug": "k20c4", "name": "K20C4", "family": "K20", "cylinders": "I4", "displacement": "2.0L", "aspiration": "Turbo", "horsepower": 200},
    {"slug": "coyote-50", "name": "Coyote 5.0L V8", "family": "Coyote", "cylinders": "V8", "displacement": "5.0L", "aspiration": "Naturally Aspirated", "horsepower": 480},
    {"slug": "ecoboost-23", "name": "EcoBoost 2.3L", "family": "EcoBoost", "cylinders": "I4", "displacement": "2.3L", "aspiration": "Turbo", "horsepower": 315},
    {"slug": "9a2-na", "name": "9A2 Flat-6 NA", "family": "9A2", "cylinders": "H6", "displacement": "4.0L", "aspiration": "Naturally Aspirated", "horsepower": 502},
    {"slug": "9a2-turbo", "name": "9A2 Turbo Flat-6", "family": "9A2", "cylinders": "H6", "displacement": "3.0L", "aspiration": "Twin-Turbo", "horsepower": 443},
    {"slug": "ea855-25t", "name": "EA855 2.5T I5", "family": "EA8", "cylinders": "I5", "displacement": "2.5L", "aspiration": "Turbo", "horsepower": 401},
    {"slug": "ea888-20t", "name": "EA888 2.0T I4", "family": "EA8", "cylinders": "I4", "displacement": "2.0L", "aspiration": "Turbo", "horsepower": 306},
    {"slug": "lt2-v8", "name": "LT2 V8", "family": "LT", "cylinders": "V8", "displacement": "6.2L", "aspiration": "Naturally Aspirated", "horsepower": 495},
    {"slug": "lt1-v8", "name": "LT1 V8", "family": "LT", "cylinders": "V8", "displacement": "6.2L", "aspiration": "Naturally Aspirated", "horsepower": 455},
]

TRANSMISSIONS = [
    {"slug": "getrag-v161", "name": "Getrag V161", "type": "Manual", "gears": 6},
    {"slug": "zf-8hp", "name": "ZF 8HP", "type": "Automatic", "gears": 8},
    {"slug": "aisin-6mt", "name": "Aisin 6-Speed Manual", "type": "Manual", "gears": 6},
    {"slug": "subaru-6mt", "name": "Subaru Performance 6-Speed Manual", "type": "Manual", "gears": 6},
    {"slug": "subaru-cvt", "name": "Subaru Lineartronic CVT", "type": "CVT", "gears": 1},
    {"slug": "bmw-m-dct", "name": "BMW M DCT", "type": "Dual-Clutch", "gears": 7},
    {"slug": "nissan-gr6", "name": "Nissan GR6", "type": "Dual-Clutch", "gears": 6},
    {"slug": "jatco-7at", "name": "JATCO 7-Speed Automatic", "type": "Automatic", "gears": 7},
    {"slug": "mazda-5mt", "name": "Mazda 5-Speed Manual", "type": "Manual", "gears": 5},
    {"slug": "mazda-6mt", "name": "Mazda 6-Speed Manual", "type": "Manual", "gears": 6},
    {"slug": "skyactiv-drive", "name": "SkyActiv-Drive 6AT", "type": "Automatic", "gears": 6},
    {"slug": "honda-6mt", "name": "Honda 6-Speed Manual", "type": "Manual", "gears": 6},
    {"slug": "honda-10at", "name": "Honda 10-Speed Automatic", "type": "Automatic", "gears": 10},
    {"slug": "getrag-mt82", "name": "Getrag MT82", "type": "Manual", "gears": 6},
    {"slug": "ford-10r80", "name": "Ford 10R80", "type": "Automatic", "gears": 10},
    {"slug": "focus-rs-6mt", "name": "Focus RS 6-Speed Manual", "type": "Manual", "gears": 6},
    {"slug": "porsche-pdk", "name": "Porsche PDK", "type": "Dual-Clutch", "gears": 7},
    {"slug": "audi-s-tronic", "name": "Audi S tronic", "type": "Dual-Clutch", "gears": 7},
    {"slug": "gm-8at", "name": "GM 8-Speed Automatic", "type": "Automatic", "gears": 8},
    {"slug": "tremec-6mt", "name": "Tremec 6-Speed Manual", "type": "Manual", "gears": 6},
]

DRIVETRAINS = [
    {"slug": "rwd", "name": "RWD"},
    {"slug": "awd", "name": "AWD"},
    {"slug": "fwd", "name": "FWD"},
]

CATEGORIES = [
    {"slug": "turbo", "name": "Turbo"},
    {"slug": "exhaust", "name": "Exhaust"},
    {"slug": "suspension", "name": "Suspension"},
    {"slug": "ecu", "name": "ECU"},
    {"slug": "brakes", "name": "Brakes"},
]

# (slug, name, manufacturer, engine, transmission, drivetrain, year, hp, torque, body_type)
CARS = [
    ("toyota-supra-mk4", "Toyota Supra MK4", "toyota", "2jz-gte", "getrag-v161", "rwd", 1993, 320, "315 lb-ft", "Coupe"),
    ("toyota-gr-supra-a90", "Toyota GR Supra", "toyota", "b58b30", "zf-8hp", "rwd", 2020, 382, "368 lb-ft", "Coupe"),
    ("toyota-gr86", "Toyota GR86", "toyota", "fa24", "aisin-6mt", "rwd", 2022, 228, "184 lb-ft", "Coupe"),
    ("bmw-m3-g80", "BMW M3", "bmw", "s58", "bmw-m-dct", "rwd", 2021, 473, "406 lb-ft", "Sedan"),
    ("bmw-m340i", "BMW M340i", "bmw", "b58b30", "zf-8hp", "rwd", 2022, 382, "369 lb-ft", "Sedan"),
    ("bmw-m2-competition", "BMW M2 Competition", "bmw", "s58", "bmw-m-dct", "rwd", 2020, 453, "406 lb-ft", "Coupe"),
    ("bmw-z4-m40i", "BMW Z4 M40i", "bmw", "b58b30", "zf-8hp", "rwd", 2021, 382, "369 lb-ft", "Convertible"),
    ("nissan-gtr", "Nissan GT-R", "nissan", "vr38dett", "nissan-gr6", "awd", 2021, 565, "467 lb-ft", "Coupe"),
    ("nissan-gtr-nismo", "Nissan GT-R Nismo", "nissan", "vr38dett", "nissan-gr6", "awd", 2022, 600, "481 lb-ft", "Coupe"),
    ("nissan-370z", "Nissan 370Z", "nissan", "vq37vhr", "jatco-7at", "rwd", 2020, 332, "270 lb-ft", "Coupe"),
    ("mazda-rx7-fd", "Mazda RX-7 (FD)", "mazda", "13b-rew", "mazda-5mt", "rwd", 1999, 255, "217 lb-ft", "Coupe"),
    ("mazda-rx8", "Mazda RX-8", "mazda", "13b-msp", "mazda-6mt", "rwd", 2004, 232, "159 lb-ft", "Coupe"),
    ("mazda3-turbo", "Mazda3 Turbo", "mazda", "skyactiv-g25t", "skyactiv-drive", "awd", 2021, 250, "320 lb-ft", "Hatchback"),
    ("honda-civic-type-r", "Honda Civic Type R", "honda", "k20c1", "honda-6mt", "fwd", 2023, 315, "310 lb-ft", "Hatchback"),
    ("honda-civic-si", "Honda Civic Si", "honda", "k20c4", "honda-6mt", "fwd", 2022, 200, "192 lb-ft", "Sedan"),
    ("honda-accord-sport-2.0t", "Honda Accord Sport 2.0T", "honda", "k20c4", "honda-10at", "fwd", 2021, 252, "273 lb-ft", "Sedan"),
    ("ford-mustang-gt", "Ford Mustang GT", "ford", "coyote-50", "getrag-mt82", "rwd", 2022, 480, "420 lb-ft", "Coupe"),
    ("ford-mustang-ecoboost", "Ford Mustang EcoBoost", "ford", "ecoboost-23", "ford-10r80", "rwd", 2021, 315, "350 lb-ft", "Coupe"),
    ("ford-focus-rs", "Ford Focus RS", "ford", "ecoboost-23", "focus-rs-6mt", "awd", 2018, 350, "350 lb-ft", "Hatchback"),
    ("porsche-911-gt3", "Porsche 911 GT3", "porsche", "9a2-na", "porsche-pdk", "rwd", 2022, 502, "346 lb-ft", "Coupe"),
    ("porsche-911-carrera-s", "Porsche 911 Carrera S", "porsche", "9a2-turbo", "porsche-pdk", "rwd", 2021, 443, "390 lb-ft", "Coupe"),
    ("porsche-cayman-gt4", "Porsche Cayman GT4", "porsche", "9a2-na", "porsche-pdk", "rwd", 2022, 414, "309 lb-ft", "Coupe"),
    ("audi-rs3", "Audi RS3", "audi", "ea855-25t", "audi-s-tronic", "awd", 2022, 401, "369 lb-ft", "Sedan"),
    ("audi-s3", "Audi S3", "audi", "ea888-20t", "audi-s-tronic", "awd", 2022, 306, "295 lb-ft", "Sedan"),
    ("audi-tt-rs", "Audi TT RS", "audi", "ea855-25t", "audi-s-tronic", "awd", 2021, 394, "354 lb-ft", "Coupe"),
    ("subaru-brz", "Subaru BRZ", "subaru", "fa24", "aisin-6mt", "rwd", 2022, 228, "184 lb-ft", "Coupe"),
    ("subaru-wrx-sti", "Subaru WRX STI", "subaru", "fa24dit", "subaru-6mt", "awd", 2021, 310, "290 lb-ft", "Sedan"),
    ("subaru-impreza-wrx", "Subaru Impreza WRX", "subaru", "fa24dit", "subaru-cvt", "awd", 2022, 271, "258 lb-ft", "Sedan"),
    ("chevrolet-corvette-stingray", "Chevrolet Corvette Stingray", "chevrolet", "lt2-v8", "gm-8at", "rwd", 2023, 495, "470 lb-ft", "Coupe"),
    ("chevrolet-camaro-ss", "Chevrolet Camaro SS", "chevrolet", "lt1-v8", "tremec-6mt", "rwd", 2022, 455, "455 lb-ft", "Coupe"),
]

# hand-curated cross-manufacturer "similar" pairs - rivals, siblings, or
# shared-platform relatives. Rendered as directed SIMILAR_TO edges.
SIMILAR_PAIRS = [
    ("toyota-gr-supra-a90", "bmw-m340i"),
    ("toyota-supra-mk4", "mazda-rx7-fd"),
    ("toyota-gr86", "subaru-brz"),
    ("subaru-brz", "toyota-gr86"),
    ("nissan-gtr", "chevrolet-corvette-stingray"),
    ("honda-civic-type-r", "ford-focus-rs"),
    ("honda-civic-type-r", "subaru-wrx-sti"),
    ("ford-mustang-gt", "chevrolet-camaro-ss"),
    ("chevrolet-camaro-ss", "ford-mustang-gt"),
    ("porsche-911-gt3", "porsche-cayman-gt4"),
    ("porsche-cayman-gt4", "porsche-911-gt3"),
    ("audi-rs3", "audi-s3"),
    ("audi-tt-rs", "audi-rs3"),
    ("nissan-370z", "mazda-rx8"),
    ("bmw-m3-g80", "bmw-m2-competition"),
    ("bmw-m2-competition", "audi-tt-rs"),
    ("subaru-wrx-sti", "subaru-impreza-wrx"),
]

# (slug, name, category, description, price_estimate, [compatible engine slugs])
UPGRADES = [
    ("garrett-gtx3076r", "Garrett GTX3076R Turbo Upgrade", "turbo", "Ball-bearing drop-in turbo upgrade for high-boost street and track builds.", "$2,400", ["2jz-gte", "s58"]),
    ("hks-gt-rs-turbine", "HKS GT-RS Turbine Kit", "turbo", "Twin-turbo replacement kit tuned for spool response without sacrificing top-end power.", "$3,800", ["vr38dett", "vq37vhr"]),
    ("precision-6266", "Precision 6266 Ball Bearing Turbo", "turbo", "High-flow single turbo swap built for four-cylinder platforms chasing big numbers.", "$1,950", ["k20c1", "ecoboost-23"]),
    ("borgwarner-efr7163", "BorgWarner EFR 7163", "turbo", "Compact frame turbo with a dual-ceramic ball bearing cartridge for near-instant spool.", "$2,100", ["fa24dit", "ea888-20t"]),
    ("ihi-vf-series", "IHI VF Series Turbo Upgrade", "turbo", "Direct-fit sequential-style turbo upgrade tuned for rotary powerbands.", "$1,600", ["13b-rew"]),
    ("akrapovic-titanium", "Akrapovic Titanium Cat-Back Exhaust", "exhaust", "Full titanium system that trims weight while opening up the exhaust note.", "$3,200", ["s58", "9a2-na"]),
    ("borla-atak", "Borla ATAK Cat-Back System", "exhaust", "Stainless cat-back tuned for an aggressive, track-ready V8 exhaust note.", "$1,100", ["coyote-50", "lt1-v8"]),
    ("hks-hipower-specl", "HKS Hi-Power Spec-L Exhaust", "exhaust", "Legendary JDM cat-back known for its deep, resonant tone.", "$1,450", ["2jz-gte", "13b-rew"]),
    ("milltek-sport", "Milltek Sport Cat-Back Exhaust", "exhaust", "OE+ fitment cat-back with a valved option for street/track flexibility.", "$1,800", ["ea855-25t", "ea888-20t"]),
    ("invidia-q300", "Invidia Q300 Cat-Back", "exhaust", "Budget-friendly stainless cat-back popular on Japanese four-cylinder platforms.", "$650", ["fa24", "k20c1"]),
    ("kw-v3-coilovers", "KW Variant 3 Coilovers", "suspension", "Independently adjustable rebound and compression damping for road and track.", "$2,600", ["b58b30", "s58"]),
    ("ohlins-road-track", "Öhlins Road & Track Coilovers", "suspension", "Motorsport-derived coilover kit offering track-level adjustability on the street.", "$3,400", ["9a2-na", "9a2-turbo"]),
    ("bilstein-b16", "Bilstein B16 PSS10 Coilovers", "suspension", "10-way adjustable damping with a factory-style ride quality baseline.", "$2,200", ["vr38dett", "lt2-v8"]),
    ("tein-flex-z", "Tein Flex Z Coilovers", "suspension", "Entry-level coilover kit balancing daily comfort with sharper handling.", "$1,050", ["fa24", "fa24dit"]),
    ("whiteline-sway-kit", "Whiteline Adjustable Sway Bar Kit", "suspension", "Front and rear adjustable sway bars to dial in handling balance.", "$480", ["k20c1", "k20c4"]),
    ("cobb-accessport", "COBB Accessport ECU Flash", "ecu", "Plug-and-play ECU flashing device with off-the-shelf performance maps.", "$720", ["fa24dit", "k20c1", "ecoboost-23"]),
    ("hp-tuners-mpvi3", "HP Tuners MPVI3", "ecu", "Professional-grade tuning interface for deep GM ECU calibration access.", "$500", ["coyote-50", "lt2-v8", "lt1-v8"]),
    ("ecutek-proecu", "EcuTek ProECU Tuning Suite", "ecu", "Full ECU reflash solution supporting custom maps for JDM turbo platforms.", "$950", ["2jz-gte", "vr38dett"]),
    ("apr-stage2", "APR Stage 2 ECU Tune", "ecu", "Bundled ECU software and hardware upgrade path for VAG turbo engines.", "$800", ["ea855-25t", "ea888-20t"]),
    ("bms-jb4", "BMS JB4 Piggyback Tuner", "ecu", "Piggyback tuning unit with switchable maps and datalogging.", "$420", ["b58b30", "s58"]),
    ("brembo-gt-6piston", "Brembo GT 6-Piston Big Brake Kit", "brakes", "Monoblock 6-piston front calipers with two-piece rotors for serious stopping power.", "$3,600", ["s58", "vr38dett"]),
    ("stoptech-st60", "StopTech ST-60 Big Brake Kit", "brakes", "6-piston front big brake kit built for repeated heavy track use.", "$2,900", ["coyote-50", "lt1-v8"]),
    ("porsche-pccb", "Porsche Ceramic Composite Brakes", "brakes", "Factory-grade carbon-ceramic rotors offering low fade and reduced unsprung weight.", "$8,900", ["9a2-na", "9a2-turbo"]),
    ("ebc-yellowstuff", "EBC Yellowstuff Performance Pads", "brakes", "High-friction street/track pad compound with minimal rotor wear.", "$180", ["fa24", "fa24dit"]),
    ("alcon-monobloc", "Alcon Monobloc Caliper Kit", "brakes", "Motorsport-derived monobloc calipers for maximum pedal feel and rigidity.", "$4,200", ["2jz-gte", "k20c1"]),
]
