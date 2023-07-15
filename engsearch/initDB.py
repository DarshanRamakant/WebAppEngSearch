import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'engsearch.settings')
import django
django.setup()
from projects.models import SeatMetrixDb

clg_data = [{"name": "SKSJTInstituteofEngineering.Bangalore", "code": "E002", "CE": "79785", "CS": "10946", "EC": "23106", "ST": "67508", "TX": "106675"}, {"name": "BMSCollegeofEngineeringBasavanagudi", "CE": "45354", "EC": "1898", "EE": "10376", "IM": "43625", "ME": "28283"}, {"name": "Dr.AmbedkarInstituteOfTechnologyBangalore", "code": "E004", "CE": "89354", "CS": "7278", "EC": "17921", "EE": "36725", "EI": "53334", "ET": "42943", "IM": "68060", "ME": "94026"}, {"name": "R.V.CollegeofEngineeringBangalore", "code": "E005", "AI": "336", "BT": "4914", "CE": "20624", "CH": "9725", "CS": "158", "CY": "368", "DS": "287", "EC": "776", "EE": "2095", "EI": "4347", "ET": "2795", "IE": "268", "IM": "22207", "ME": "7320", "SE": "2153"}, {"name": "MSRamaiahInstituteofTechnologyBangalore", "code": "E006", "AI": "2124", "BT": "9284", "CE": "39775", "CH": "23930", "CS": "827", "CY": "1840", "EC": "3020", "EE": "8465", "EI": "11470", "ET": "7449", "IE": "1534", "IM": "42492", "MD": "18041", "ME": "29510"}, {"name": "DayanandaSagarCollegeofEngineering Bangalore", "code": "E007", "AE": "14957", "AI": "4830", "AU": "58059", "BT": "18131", "CB": "6744", "CD": "6962", "CE": "77366", "CH": "39485", "CS": "3100", "CY": "5333", "DS": "5159", "EC": "9179", "EE": "27286", "EI": "30561", "ET": "26912", "IE": "4668", "MD": "37604", "ME": "69265"}, {"name": "BangaloreInstituteofTechnologyBangalore", "code": "E008", "AI": "6629", "CE": "86418", "CS": "3747", "DS": "5469", "EC": "10265", "EE": "23990", "EI": "37332", "ET": "24817", "EV": "22091", "IE": "5573", "IO": "7599", "ME": "72953", "RI": "11595"}, {"name": "PESUniversity(RingRoadCampus)Bangalore", "code": "E009", "AI": "1301", "BT": "7692", "CS": "787", "EC": "3366", "EE": "7923", "ME": "13742"}, {"name": "MVJCollegeofEngineeringBangalore", "code": "E011", "AE": "56762", "AI": "25248", "CD": "31596", "CE": "115355", "CH": "79412", "CS": "16694", "DS": "26663", "EC": "33654", "EE": "59860", "IE": "21176", "ME": "108871", "SE": "46685", "TI": "98692"}, {"name": "SirM.VisveswarayaInstituteofTechnologyHunasemaranahalli", "AI": "12196", "BT": "28846", "CE": "94674", "CS": "7806", "EC": "16167", "EE": "42935", "ET": "40416", "IE": "10576", "IO": "13448", "ME": "100567"}, {"name": "GhousiaEngineeringCollegeRamanagara", "code": "E013", "CE": "174068", "CS": "65903", "EC": "82065", "EE": "101471", "IE": "76168", "ME": "169340"}, {"name": "SJCInstituteofTechnologyChickballapur", "code": "E014", "AE": "43460", "Le": "34208", "CD": "50134", "CE": "116427", "CK": "171550", "CS": "22526", "EC": "48019", "IE": "32149", "ME": "113878", "SE": "52319"}, {"name": "Dr.T.ThimmaiahInstituteofTechnologyBANGARAPET-TQkolar District", "code": "E015", "CA": "96716", "CE": "171627", "CS": "44717", "EC": "83774", "EE": "93357", "ME": "155159", "MN": "163883"}, {"name": "SiddagangaInstituteofTechnology  Tumkur", "code": "E016", "AD": "30729", "CE": "56247", "CH": "63708", "CS": "5050", "EC": "10890", "EE": "20592", "EI": "27292", "ET": "20042", "IE": "7046", "IM": "68018", "ME": "73010"}, {"name": "SriSiddarthaInstituteofTechnology  Tumkur", "code": "E017", "AI": "42790", "CE": "115087", "CS": "26902", "DS": "35824", "EC": "44082", "EE": "79505", "ET": "69069", "IE": "34820", "MD": "82260", "ME": "173788"}, {"name": "KalpatharuInstituteofTechnology  Tiptur", "code": "E018", "CE": "172089", "CS": "37832", "EC": "70063", "IE": "54036", "ME": "156885"}, {"name": "SriJayachamarajendraCollegeofEngineering(Const.ofJSSUniv.)  Mysore", "code": "E021", "CE": "46604", "CS": "1567", "EC": "5679", "EE": "16708", "EI": "22768", "EN": "61885", "IP": "72605", "ME": "45271", "PT": "88322"}, {"name": "TheNationalInstituteofEngineering(SOUTHCAMPUS)  Mysore", "code": "E022", "CE": "68623", "EC": "8260", "ME": "42151"}, {"name": "PESCollegeofEngineering Mandya", "code": "E023", "AU": "79940", "CE": "108706", "EC": "20222", "EE": "38017", "IP": "97040"}, {"name": "PESCollegeofEngineering Mandya", "code": "E023", "ME": "119017"}, {"name": "MalnadCollegeofEngineering  Hassan", "code": "E024", "CE": "89844", "EC": "22240", "EE": "44747", "ME": "172022"}, {"name": "TontadaryaCollegeofEngineering  Gadag", "code": "E028", "CD": "72617", "CE": "144947", "CS": "45571", "EA": "77325", "EC": "59781", "EE": "81588", "ME": "166049"}, {"name": "MarathaMandalEngineeringCollege  Belgaum", "code": "E029", "CS": "51614", "EC": "62897", "ME": "166142", "RI": "81812"}, {"name": "KLETechnologicalUniversity(FormerlyBVBCET)  Hubli", "code": "E030", "CE": "42964", "EC": "7073", "EE": "21259", "ME": "46307"}, {"name": "BasaveshwaraEngineeringCollegeBagalkot", "code": "E031", "CE": "83485", "CS": "14937", "EC": "24241", "EE": "47088", "IP": "126891", "ME": "173608"}, {"name": "R.T.ESocity`sRuralEngineeringCollege  Hulkoti", "code": "E032", "CE": "173135", "CS": "54384", "EC": "76583", "ME": "164584", "TX": "172007"}, {"name": "SriTaralabaluJagadguruInstituteofTechnology.  Ranebennur", "code": "E033", "CE": "168380", "CS": "51836", "EC": "72828", "EE": "100108"}, {"name": "SriTaralabaluJagadguruInstituteofTechnology.  Ranebennur", "code": "E033", "IE": "69315"}, {"name": "SriDharmasthalaManjunatheswaraCollegeofEngineering  Dharwad", "code": "E034", "AI": "18594", "CE": "82293", "CH": "50009", "CS": "8813", "EC": "15556", "EE": "30464", "IE": "11580", "ME": "101613"}, {"name": "AnjumanEngineeringCollegeBhatkala", "CE": "145214", "CS": "63503", "EC": "96179", "EE": "172332", "ME": "162484"}, {"name": "KLETechnologicalUniversity(FormerlyKLEDr.MSSheshagiriCol.)  Belgaum", "code": "E036", "BM": "45718", "CE": "99806", "CF": "19922", "CH": "65602", "CS": "15721", "EC": "21888", "EE": "43165", "ME": "99449"}, {"name": "K.L.S.GogteInstituteofTechnology  Belgaum", "code": "E037", "AE": "39419", "CE": "73183", "CS": "9044", "EC": "16685", "EE": "32718", "IE": "11676", "ME": "74015"}, {"name": "BLDEAsV.P.Dr.P.G.HallakattiCollegeofEngg.andTech.  vijayapur", "code": "E038", "CE": "96413", "CS": "28158", "EC": "41965", "EE": "58392", "IE": "35956", "ME": "165658"}, {"name": "HiraSugarInstituteofTechnologyBelagavi District"}, {"name": "HiraSugarInstituteofTechnologyBelagavi District", "CE": "172351", "CS": "38931", "EC": "55701", "EE": "91061", "ME": "174294"}, {"name": "PDACollegeofEngineeringGulbarga", "code": "E041", "CE": "75505", "EC": "33418", "EE": "55868", "IP": "173186", "ME": "173095"}, {"name": "KhajaBandaNawazUniversityKalburgi", "code": "E042", "AE": "80843", "CE": "174141", "CS": "46336", "EC": "59780", "ME": "161696"}, {"name": "GurunanakDevEngineeringCollege  Bidar", "code": "E043", "AI": "65938", "CE": "154108", "CS": "30768", "DS": "62530", "EC": "71615", "EE": "95769", "IE": "50946", "ME": "167946"}, {"name": "BheemannaKhandreInstituteofTechnology  Bhalki", "code": "E044", "Le": "59223", "CE": "171541", "CH": "158947", "CK": "38442", "DS": "66365", "EC": "77077", "ME": "158956", "RI": "83777"}, {"name": "RaoBahadurY.MahabaleswarappaEngineeringCollege  Bellari", "code": "E045", "Le": "64244", "CE": "173030", "CS": "38284", "DS": "71189", "EC": "66939"}, {"name": "RaoBahadurY.MahabaleswarappaEngineeringCollege  Bellari", "code": "E045", "EE": "100168", "IE": "59470", "ME": "174064"}, {"name": "HKEsSLNCollegeofEngineering  Raichur", "code": "E046", "CE": "171913", "CS": "55626", "EC": "88969"}, {"name": "MalnadCollegeofEngineering  Hassan", "code": "E047", "Le": "16146", "CB": "25933", "CE": "95176", "CS": "12041", "EC": "25695", "EE": "47678", "EI": "65506", "IE": "19053", "ME": "172883"}, {"name": "BMSCollegeofEngineeringBasavanagudi", "AI": "1998", "BT": "11265", "CE": "46207", "CH": "30525", "CS": "841", "DS": "1403", "EC": "3463", "EI": "8821", "ET": "5467", "IE": "1363", "IO": "1538", "MD": "19714", "ME": "27610", "SE": "4829"}, {"name": "BasaveshwaraEngineeringCollegeBagalkot", "code": "E049", "AI": "31191", "BT": "60009", "CE": "101398", "CS": "18486", "EC": "28656", "IE": "23849"}, {"name": "KVGCollegeofEngineeringSullia", "Le": "76555", "CE": "143012", "CS": "59690", "EC": "76015", "ME": "171683"}, {"name": "PACollegeofEngineeringBantwal", "AI": "66416", "BT": "96005", "CS": "63031", "EC": "89760", "ME": "163355"}, {"name": "TheNationalInstituteofEngineering(SOUTHCAMPUS)  Mysore", "code": "E056", "EC": "9363", "EE": "20560", "ME": "55260"}, {"name": "JSSScienceandTechnologyUniversity(FormerlySJCE)  Mysore", "code": "E057", "BT": "22080", "CB": "4823", "CE": "68752", "CS": "2575", "CT": "68015", "EC": "6682", "IE": "3605", "ME": "51545"}, {"name": "PESCollegeofEngineering Mandya", "code": "E058", "AU": "84869", "Le": "20024", "CE": "88597", "CS": "14021", "EC": "25050", "EE": "40499", "IE": "17089"}, {"name": "PDACollegeofEngineeringGulbarga", "code": "E059", "AI": "40339", "CD": "38478", "CE": "101979", "CR": "151484", "CS": "20819", "EC": "36912", "EE": "50374"}, {"name": "PDACollegeofEngineeringGulbarga", "code": "E059", "EG": "164405", "EI": "86929", "IE": "31976", "IP": "163019", "ME": "168042"}, {"name": "Dr.AmbedkarInstituteOfTechnologyJnanabharathiCampus", "AE": "37739", "AI": "14685", "CB": "21184", "CE": "95979", "CS": "10815", "EC": "20159", "IE": "12866"}, {"name": "UniversityB.D.T.collegeofEngineering Davangere", "code": "E061", "CE": "85696", "CS": "14132", "EC": "28580", "EE": "42826", "EI": "72460", "IP": "114642", "ME": "111868"}, {"name": "BapujiInstituteofEngineeringandTechnology  Davangere", "code": "E062", "AI": "33763", "BT": "55240", "CB": "38020", "CD": "43105", "CE": "103384", "CH": "73168", "CS": "15476", "DS": "31045", "EC": "30295", "EE": "51915", "IE": "28004", "ME": "160025", "TX": "149928"}, {"name": "SriJagadguruMurugharajendraUniversity(FormerlySJMIT)  Chitradurga", "code": "E063", "CE": "147066", "CS": "50891", "EC": "73626", "EE": "99767", "ME": "172965"}, {"name": "AdhichunchanagiriInstituteofTechnologyChickmagalur", "code": "E064"}, {"name": "AdhichunchanagiriInstituteofTechnologyChickmagalur", "code": "E064", "AI": "42389", "CE": "160031", "CS": "25408", "DS": "43928", "EC": "48137", "EE": "84981", "IE": "33138", "ME": "136295"}, {"name": "JawaharlalNehruNationalCollegeofEngineering  Shimoga", "code": "E065", "AI": "26318", "CE": "172686", "CS": "14453", "EC": "36124", "EE": "68937", "ET": "66296", "IE": "25161", "ME": "169137", "RI": "68011"}, {"name": "BahubaliCollegeofEngineeringHassan Dist", "AI": "85955", "CE": "173940", "CS": "66307", "EC": "81380", "IE": "79107", "ME": "162298"}, {"name": "VidyaVardhakaCollegeofEngineering  Mysuru", "code": "E071", "CE": "79906", "CS": "9993", "EC": "19077", "EE": "29405", "IE": "12596", "ME": "92896"}, {"name": "BallariInstituteofTechnologyandManagementNearAllipur Bellary", "code": "E075", "AI": "46884", "CE": "133797", "CF": "35419", "CS": "19536", "DS": "33009", "EC": "44260", "EE": "82044", "ME": "171229"}, {"name": "ProudadevarayaInstituteofTechnologyIndiranagarHospet", "Le": "70234", "CE": "162025", "CS": "55416", "EC": "77069", "EE": "117855", "ME": "166994"}, {"name": "VidyaVikasInstituteofEngineeringandTechnology  Mysuru", "code": "E077", "CE": "114376", "CS": "24405", "EC": "35425", "EE": "58453", "IE": "31286", "ME": "111279"}, {"name": "TheOxfordCollegeofEngineeringBangalore", "code": "E078", "AI": "35346", "BT": "56864", "CE": "169753", "CS": "24522", "EC": "44698", "EE": "72425", "IE": "32847", "ME": "170054", "MT": "135298"}, {"name": "AcharyaInstituteofTechnologyBangalore", "code": "E079", "AE": "38092", "AI": "25845", "BT": "42168", "CE": "102328", "CS": "14749", "DS": "23221", "EC": "27737", "EE": "46999", "IE": "17663", "ME": "112286", "MT": "88747"}, {"name": "HMSInstituteofTechnology  Tumkur", "code": "E081", "CE": "171484", "CS": "63134", "EC": "78806", "EE": "106582", "ME": "156995"}, {"name": "JSSAcademyofTechnicalEducationBangalore", "code": "E082", "Le": "16303"}, {"name": "JSSAcademyofTechnicalEducationBangalore", "code": "E082", "CE": "109611", "CS": "10213", "EC": "24351", "EI": "47099", "IE": "14046", "ME": "110948", "RA": "30063"}, {"name": "H.K.B.K.CollegeofEngineeringBangalore", "code": "E083", "AI": "53536", "CS": "39398", "EC": "69082", "IE": "49784", "ME": "172529"}, {"name": "APSCollegeofEngineeringSomanahalli", "CE": "171116", "CS": "32614", "EC": "58401", "IE": "45857", "ME": "173443"}, {"name": "SriSairamCollegeofEngineering(FormerlyShirdiSaiEngg)Anekal", "AI": "55187", "CS": "43120", "EC": "69907", "EE": "74453", "IE": "53332", "ME": "155634"}, {"name": "VivekananadaInstituteofTechnologyBangalore", "code": "E087", "AI": "54009", "CE": "167674", "CS": "36937", "EC": "55882", "IE": "46753", "ME": "171810"}, {"name": "BangaloreCollegeofEngineeringandTechnologyChandapura", "AI": "60768", "CS": "33655", "EC": "61522", "EE": "83581", "IE": "48524"}, {"name": "SriRevanaSiddeswaraInstituteofTechnologyBangalore North", "code": "E090", "CE": "147447"}, {"name": "SriRevanaSiddeswaraInstituteofTechnologyBangalore North", "code": "E090", "CS": "36296", "EC": "68924", "ME": "169722"}, {"name": "KSInstituteofTechnologyBangalore", "code": "E091", "AI": "32947", "CC": "45579", "CD": "39585", "CS": "24364", "EC": "41839", "IO": "38009", "ME": "173699"}, {"name": "VemanaInstituteofTechnologyBangalore", "code": "E092", "AI": "51739", "CE": "174070", "CS": "36955", "EC": "64264", "IE": "48309", "ME": "163058"}, {"name": "BasavakalyanaEngineeringCollegeBasavakalyana", "CE": "169649", "CS": "62279", "EC": "87319"}, {"name": "CoorgInstituteofTechnology  Kodagu", "code": "E094", "AI": "82372", "CE": "158657", "CS": "45507", "EC": "77627", "ME": "137676"}, {"name": "AMCEngineeringCollegeBangalore", "code": "E095", "AE": "67403", "AI": "41424", "CE": "147261", "CS": "30869", "DS": "46082", "EC": "52263", "EE": "70586", "IE": "38330"}, {"name": "AMCEngineeringCollegeBangalore", "code": "E095", "ME": "173507", "MT": "161957"}, {"name": "EastPointCollegeofEngineeringandTechnology  Bangalore", "code": "E096", "AD": "118532", "CS": "33328", "EC": "61906", "IE": "48106", "IO": "63860", "ME": "173506"}, {"name": "CMRInstituteofTechnologyBangalore", "code": "E097", "AD": "30818", "AI": "20394", "Le": "16174", "CS": "10280", "DS": "17165", "EC": "25023", "IE": "14017"}, {"name": "AtriaInstituteofTechnologyBangalore", "code": "E098", "CD": "49355", "CE": "170689", "CS": "23976", "DS": "35738", "EC": "52042", "IE": "33170", "ME": "173245"}, {"name": "NewHorizonCollegeofEngineeringBangalore", "code": "E099", "AI": "15969", "CE": "87546", "CO": "16177", "CS": "6932", "DS": "13676", "EC": "18747", "EE": "45125", "IE": "11176", "ME": "86827"}, {"name": "KNSInstituteofTechnologyBangalore", "code": "E100", "AI": "67697"}, {"name": "KNSInstituteofTechnologyBangalore", "code": "E100", "CE": "170109", "CS": "49932", "DS": "68206", "EC": "71640", "IE": "58011"}, {"name": "ChannabasaveshwaraInstituteofTechnologyGubbi", "AD": "159207", "CS": "33562", "EC": "59653", "EE": "79885", "IE": "44179", "ME": "170125"}, {"name": "DONBOSCOInstituteofTechnologyBangalore", "code": "E102", "AD": "43882", "CE": "170469", "CS": "26411", "EC": "47195", "EE": "69945", "IE": "35235", "ME": "166230"}, {"name": "GlobalAcademyofTechnologyBangalore", "code": "E103", "AD": "47718", "AI": "25774", "CE": "122221", "CS": "17211", "EC": "31763", "EE": "61660", "IE": "21761", "ME": "139145"}, {"name": "NagarjunaCollegeofEngineeringandTechnologyBangalore (R)", "code": "E104", "CE": "174164", "CS": "36759", "DS": "58924", "EC": "61659", "IE": "45269"}, {"name": "NitteMeenakshiInstitututeofTechnology Bangalore", "code": "E105"}, {"name": "NitteMeenakshiInstitututeofTechnology Bangalore", "code": "E105", "AD": "35370", "AI": "10768", "CE": "100785", "CS": "6702", "EC": "14579", "EE": "41503", "IE": "9419", "ME": "88919"}, {"name": "EastWestInstituteofTechnologyBangalore", "code": "E106", "AI": "52878", "CE": "174075", "CS": "33290", "EC": "59667", "EE": "80675", "IE": "43727", "IO": "60007", "ME": "169077"}, {"name": "BNMInstituteofTechnologyBangalore", "code": "E107", "AI": "12186", "CS": "7448", "EC": "16299", "EE": "37294", "IE": "8610", "ME": "102921"}, {"name": "SapthagiriCollegeofEngineeringBangalore", "code": "E108", "BT": "65995", "CE": "169819", "CS": "20597", "EC": "37154", "EE": "78312", "IE": "26283", "ME": "170399"}, {"name": "CityEngineeringCollegeBangalore", "code": "E109", "AI": "65928", "CE": "171493", "CS": "51644", "EC": "74137", "IE": "62376", "ME": "174272"}, {"name": "SriVenkateshwaraCollegeofEngineeringBettahalsur(P)"}, {"name": "SriVenkateshwaraCollegeofEngineeringBettahalsur(P)", "CE": "171519", "CF": "48351", "CS": "35591", "CY": "60303", "DS": "54848", "EC": "63156", "IE": "45100", "ME": "170792"}, {"name": "SriKrishnaInstituteofTechnologyBangalore", "code": "E112", "AI": "65341", "CE": "168078", "CS": "49969", "EC": "69470", "IE": "57385", "ME": "161949"}, {"name": "SambhramInstituteofTechnologyBangalore", "code": "E113", "AI": "70529", "CE": "173381", "CS": "55811", "CY": "69534", "EC": "75656", "IE": "61810", "ME": "162858"}, {"name": "GMInstituteofTechnologyDavanagere", "code": "E114", "AI": "44960", "BT": "83423", "CE": "146986", "CS": "22508", "EC": "40008", "EE": "65717", "IE": "30992", "ME": "174051", "RA": "86374"}, {"name": "SJBInstituteofTechnologyKengeri", "AI": "21822", "CE": "138997", "CS": "14602", "DS": "21432", "EC": "26753", "EE": "55005"}, {"name": "SJBInstituteofTechnologyKengeri", "IE": "18134", "ME": "131313"}, {"name": "R.L.JalappaInstituteofTechnologyBangalore Rural Dist", "code": "E116", "Le": "76406", "CS": "51177", "DS": "74914", "EC": "82167", "ME": "168442"}, {"name": "RNSInstituteofTechnologyBangalore", "code": "E118", "AI": "15339", "CE": "103861", "CS": "6979", "CY": "14523", "DS": "12831", "EC": "17237", "EE": "37840", "IE": "9718", "ME": "103139"}, {"name": "KCTEngineeringCollegeRoza(B)", "CE": "160419", "CS": "52490", "EC": "79208"}, {"name": "JnanavikasaInstituteofTechnologyRamanagar-Dist", "code": "E120", "CE": "170066", "CS": "61417", "EC": "82208"}, {"name": "VivekananadaCollegeofEngineeringTechnology  D K DIST", "code": "E121", "AI": "54383", "CE": "154437", "CS": "33471", "DS": "49138", "EC": "67275", "ME": "167945"}, {"name": "CanaraEngineeringCollegeBantwal  DK DIST", "code": "E123", "AI": "48876"}, {"name": "CanaraEngineeringCollegeBantwal  DK DIST", "code": "E123", "CB": "59789", "CD": "64814", "CS": "33023", "EC": "59745", "IE": "40117"}, {"name": "RajivGandhiInstituteofTechnologyR.TNagarPost", "BM": "76439", "CE": "172496", "CS": "47470", "EC": "67686", "EE": "94107", "ME": "147319"}, {"name": "BMSInstituteofTechnologyandManagementYelahanka", "AI": "9162", "CE": "83099", "CS": "4191", "EC": "11500", "EE": "30548", "ET": "23653", "IE": "6926", "ME": "59527"}, {"name": "MSEngineeringCollegeBangalore Urban", "code": "E127", "AI": "70106", "CE": "171184", "CS": "63711", "EC": "71335"}, {"name": "SharnbasvaUniversity(FormerlyAppaInst.ofTech.)Brahmpur", "CE": "172832", "CS": "29940", "EC": "49639", "EE": "57606", "EG": "160160", "ME": "169308"}, {"name": "St.JosephEngineeringCollegeMangalore", "code": "E129", "AI": "20298", "CB": "26824", "CE": "173534", "CS": "16331"}, {"name": "St.JosephEngineeringCollegeMangalore", "code": "E129", "DS": "20082", "EC": "38783", "EE": "70251", "ME": "174151"}, {"name": "ShrideviInstituteofEngineeringandTechnology  Tumkur", "code": "E130", "AD": "172297", "CS": "55185", "EC": "72657", "EE": "101363", "IE": "65869", "ME": "156064"}, {"name": "SecabInstituteofEngineeringandTechnology  Bijapur", "code": "E132", "CE": "173727", "CS": "45130", "EC": "64890", "EE": "103709", "ME": "158998"}, {"name": "GSSSInstituteofEngineeringandTechnologyforWomen  Mysore", "code": "E133", "CS": "16758", "EC": "31468", "EE": "48645", "IE": "20838"}, {"name": "Smt.KamalaandSriVenkappaM.AgadiCollegeofEngg.andTech.Laxmeshwara-Tq", "CE": "157656", "CS": "40727", "EC": "60292", "EE": "102613", "IE": "55537", "ME": "171294"}, {"name": "KLSViswanathraoDeshpandeInstituteofTechnologyHaliyal", "CE": "170725", "CS": "29172", "EC": "53238", "EE": "71021", "ME": "170028"}, {"name": "MoodalakatteInstituteofTechnologyUdupi District", "code": "E136", "AI": "79978"}, {"name": "MoodalakatteInstituteofTechnologyUdupi District", "code": "E136", "CE": "172168", "CS": "62995", "DS": "88959", "EC": "86072"}, {"name": "ImpactCollegeofEngineeringandAppliedSciences  Bangalore", "code": "E139", "AI": "73996", "CE": "170708", "CS": "56246", "DS": "73170", "EC": "74197", "RO": "102713"}, {"name": "PESUniversity(ElectronicCityCampus) Bangalore", "code": "E141", "CS": "3443", "EC": "5895"}, {"name": "AdichunchanagiriUniversity(FormerlyBGSIT)NagamangalaTaluk", "AI": "49166", "CE": "174013", "CS": "30059", "EC": "43931", "IE": "37747", "ME": "163407"}, {"name": "SrinivasInstituteofTechnologyMangalore.", "code": "E144", "AE": "98227", "AI": "69844", "AU": "169965", "CB": "75422", "CD": "68175", "CS": "43297", "EC": "70336", "EE": "99450", "IE": "50935", "ME": "170490", "MR": "147062"}, {"name": "RajarajeswariCollegeofEngineeringKumbalagodu", "AI": "42682", "CE": "143296", "CS": "29858"}, {"name": "RajarajeswariCollegeofEngineeringKumbalagodu", "EC": "52599", "EE": "78696", "IE": "35144", "IO": "50235", "RA": "72385"}, {"name": "ShreedeviInstituteofTechnologyKenjar", "AE": "101425", "CE": "154151", "CS": "65915", "EC": "89141", "IE": "77826", "ME": "172298"}, {"name": "T.JohnEngineeringCollegeBangalore", "code": "E147", "AI": "65099", "CE": "151042", "CS": "48230", "EC": "63495", "IE": "57371"}, {"name": "CambridgeInstitututeofTechnologyBangalore", "code": "E149", "AI": "32365", "CE": "141570", "CS": "23622", "EC": "43377", "EE": "67427", "IE": "31437", "ME": "170539"}, {"name": "PESInstituteofTechnologyandManagement Shivamogga", "code": "E150", "AI": "46816", "CD": "62293", "CE": "171042", "CS": "28740", "DS": "49575", "EC": "51057", "EE": "81264", "IE": "34966", "ME": "170558"}, {"name": "MangaloreInstituteofTechnologyandEngineeringMangalore Tq", "AE": "61355", "AI": "35635", "CE": "161690"}, {"name": "MangaloreInstituteofTechnologyandEngineeringMangalore Tq", "CS": "21060", "EC": "49781", "IE": "28586", "IO": "40160", "ME": "170583", "MT": "167408"}, {"name": "SDMInstituteofTech.Ujire", "AD": "173542", "CS": "32238", "EC": "54971", "EE": "83836", "IE": "40235"}, {"name": "SEACollegeofEngineeringandTechnologyKRpuram bangalore", "code": "E153", "AI": "69554", "CE": "169593", "CS": "55549", "EA": "99059", "EC": "77328", "IE": "63419", "IO": "77403", "ME": "123241"}, {"name": "GovernmentEngineeringCollegeChamarajanagara", "code": "E154", "CE": "105526", "CS": "35971", "EC": "67990", "ME": "154007"}, {"name": "GovernmentEngineeringCollege  Hassan", "code": "E155", "CE": "90616", "CS": "21794", "EC": "34883", "ME": "130757"}, {"name": "GovernmentEngineeringCollegeKRPet", "CE": "112284", "CS": "37255", "EC": "60519", "ME": "172755"}, {"name": "GovernmentEngineeringCollegeRamanagara", "code": "E157", "CE": "143210", "CS": "46049", "EC": "72011"}, {"name": "GovernmentEngineeringCollegeRamanagara", "code": "E157", "MM": "172564"}, {"name": "MaharajaInstituteofTechnology-MysoreBelawadi", "CB": "47859", "CE": "141568", "CF": "35391", "CS": "26766", "DS": "41099", "EC": "40156", "IE": "34681", "ME": "126086"}, {"name": "KaravaliInstituteofTechnologyMangalore", "code": "E159", "MK": "104777", "AI": "94549", "CE": "152010", "CS": "78075", "EC": "94341"}, {"name": "SahyadriCollegeofEngg.andManagement Mangalore", "code": "E160", "CA": "33165", "CS": "12052", "DS": "23629", "EC": "32696", "IE": "19347", "ME": "122823", "RA": "68040"}, {"name": "GovernmentEngineeringCollegeKushalnagar", "CE": "155905", "CS": "43598", "EC": "65923", "ME": "173273"}, {"name": "GovernmentEngineeringCollege Raichur", "code": "E162", "CE": "120249", "CS": "34723", "EC": "67466", "ME": "171461"}, {"name": "GovernmentEngineeringCollegeDevagiri", "CE": "124627", "CS": "39939"}, {"name": "GovernmentEngineeringCollegeDevagiri", "EC": "61557", "ME": "172058"}, {"name": "GovernmentEngineeringCollegeHuvinaHadagali", "CE": "174062", "CS": "53596", "EC": "75358", "ME": "174330"}, {"name": "YenepoyaInstituteofTechnologyThodar", "AI": "82245", "CS": "54721", "EC": "85888", "EE": "119915", "IE": "68843", "IO": "82223"}, {"name": "KLEInstituteofTechnology  Hubli", "code": "E166", "CE": "83620", "CS": "15664", "EC": "25300", "EE": "41292", "ME": "122641"}, {"name": "KLESsKLECollegeofEngineeringandTechnologyChikkodi", "CE": "133807", "CS": "28819", "EC": "39724", "ME": "166730"}, {"name": "AmruthaInstituteofEngineeringandMangementBidadiIndust.Estate", "CE": "169656", "CS": "53012", "EC": "75976"}, {"name": "Alva`sInstituteofEngineeringandTechnologyMoodabidri", "AI": "48556", "CD": "62503", "CE": "168564", "CS": "36856", "DS": "49836", "EA": "92128", "EC": "58056"}, {"name": "Alva`sInstituteofEngineeringandTechnologyMoodabidri", "IE": "44236", "IO": "64074", "ME": "169050"}, {"name": "BrindavanCollegeofEngineeringYelahanka", "AI": "64841", "CE": "162459", "CS": "47942", "EC": "75815", "IE": "59740", "IO": "74676"}, {"name": "R.R.InstituteofTechnologyChikkabanavara", "CS": "46272", "EC": "69758", "EE": "91505", "IE": "53647"}, {"name": "SaiVidyaInstituteofTechnologyBangalore", "code": "E173", "Le": "46671", "CE": "156633", "CS": "24733", "DS": "50076", "EC": "57827", "IE": "34277", "ME": "168942"}, {"name": "Dr.Sri.Sri.Sri.ShivakumaraMahaswamyjiCollegeofEngineeringBangalore Rural -Dist", "CE": "163084", "CS": "69028", "EC": "78927", "EE": "100888", "IE": "76886"}, {"name": "S.G.BalekundriInstituteofTechnology  Belgaum", "code": "E175", "CB": "69535", "CE": "165851", "CS": "41600", "EC": "55505", "EE": "85221", "ME": "140457"}, {"name": "NavodayaInstituteofTechnology Raihcur", "code": "E176"}, {"name": "NavodayaInstituteofTechnology Raihcur", "code": "E176", "CE": "169621", "CS": "41573", "EC": "87213", "EE": "137722"}, {"name": "RajeevInstituteofTechnology  Hassan", "code": "E177", "Le": "65383", "CE": "172924", "CS": "42991", "EC": "59035", "EE": "88339", "IE": "53601", "ME": "113191"}, {"name": "TheNationalInstituteofEngineering(NORTHCAMPUS)  Mysore", "code": "E178", "Le": "6289", "CS": "4794", "IE": "7352"}, {"name": "BearysInstituteofTechnologyMangalore", "code": "E180", "AD": "173026", "CS": "71876", "EC": "104217", "ME": "154801"}, {"name": "Sha-ShibCollegeofEngineeringChickballapur", "code": "E183", "AE": "121029", "CE": "167602", "CS": "74799", "EC": "96205"}, {"name": "CByreGowdaInstituteofTechnology  Kolar", "code": "E184", "AI": "95488", "CE": "173856", "CS": "79517", "EC": "102977", "ME": "113132"}, {"name": "AngadiInstituteofTechnologyandManagement  Belgaum", "code": "E185", "CE": "168388", "CS": "45260", "EC": "55156", "EE": "76742", "ME": "140797"}, {"name": "AngadiInstituteofTechnologyandManagement  Belgaum", "code": "E185", "RA": "96934"}, {"name": "ACSCollegeofEngineeringKengeriHobli", "AE": "90539", "BM": "88361", "CS": "41052", "CY": "60467", "DS": "59492", "EC": "62116", "ME": "160817", "SE": "78640"}, {"name": "VijayaVittalaInstituteofTechnology Bangalore", "code": "E188", "AI": "81991", "Le": "79500", "CE": "164791", "CS": "59656", "EC": "83211"}, {"name": "NavkisCollegeofEngineering(FormerlyNDRKIT)Kandali", "AI": "52941", "CE": "167795", "CS": "39493", "EC": "57392"}, {"name": "AkshayaInstituteofTechnology  Tumkur", "code": "E191", "CE": "109695", "CS": "66566", "EA": "103855", "EC": "81681", "IE": "77494", "ME": "155269", "SA": "151208"}, {"name": "SrinivasUniversityMukka", "AI": "89178", "CE": "171139", "CS": "62407", "EC": "80234", "ME": "173169"}, {"name": "GovernmentEngineeringCollege  KARWAR", "code": "E194"}, {"name": "GovernmentEngineeringCollege  KARWAR", "code": "E194", "CE": "170835", "CS": "49995", "EC": "81580", "ME": "172212"}, {"name": "JainCollegeofEngineeringMachche", "CE": "174180", "CS": "23820", "EC": "36965", "EE": "67357", "ME": "170500"}, {"name": "VeerappaNistyEngineeringCollegeYadigir Dist", "code": "E197", "CE": "160776", "CS": "78400", "EC": "96454", "EE": "173833"}, {"name": "SharnbasvaUniversityCollegeforWomen(FormerlyGodutai)  Gulbarga", "code": "E198", "AI": "64121", "CE": "148955", "CS": "38112", "EC": "66897", "EE": "96312"}, {"name": "AGMRuralEngineeringCollegeHubli", "CE": "167511", "CS": "50218", "EC": "65133", "EE": "93199", "ME": "162597"}, {"name": "GopalanCollegeofEngineeringandManagementWhiteField", "AE": "90474", "CE": "174228", "CS": "37497", "EC": "61552", "ME": "169608"}, {"name": "SampoornaInstituteofTechnologyandResearchRamanagara (D)", "code": "E202", "CS": "73537", "EC": "93789", "EE": "121811", "ME": "169859"}, {"name": "K.S.SchoolofEngineeringAndManagementMallasandra"}, {"name": "K.S.SchoolofEngineeringAndManagementMallasandra", "CB": "69303", "CE": "137873", "CS": "44544", "EC": "76373", "ME": "128818"}, {"name": "BangaloreTechnologicalInstituteSarjapuraRd", "AI": "62028", "CE": "163601", "CS": "46792", "EC": "67682", "ME": "156568", "RI": "82351"}, {"name": "ATMECollegeofEngineeringVarunhobli", "Le": "43284", "CD": "58811", "CE": "127517", "CS": "32563", "DS": "49307", "EC": "49225", "EE": "67584", "ME": "170610"}, {"name": "ShriMadhwaVadirajaInstituteofTechnologyandManagement  Udupi Dist", "code": "E206", "AI": "54781", "CE": "170853", "CS": "29245", "EC": "74274", "ME": "168593"}, {"name": "VSMsSomashekarRKothiwaleInstituteofTechnologyNippani", "CE": "106021", "CS": "62300", "EC": "73622", "ME": "116550"}, {"name": "JyothiInstituteofTechnologyBangalore", "code": "E209", "AI": "45789", "CE": "173729", "CS": "33177", "EC": "65709", "IE": "42665", "ME": "173406"}, {"name": "GMadegowdaInstituteofTechnologyMaddurTaluk", "AI": "86724", "CE": "173078", "CS": "60912", "EC": "81372", "EE": "108285", "ME": "173743"}, {"name": "JainInstituteofTechnologyCross", "CE": "172490", "CS": "39793", "EC": "55579", "EE": "87394", "IE": "49088", "ME": "141846"}, {"name": "DayanandaSagarAcademyofTechnologyKanakapurMainRoad Bangalore", "code": "E212", "Le": "19269", "CD": "27190", "CE": "112131", "CF": "21975", "CS": "13450", "DS": "18743", "EC": "26294", "EE": "55571", "IE": "17967", "IO": "26552", "ME": "123108"}, {"name": "LingarajappaEngineeringCollege  Bidar", "code": "E213", "CS": "64575", "EC": "93023", "EE": "173523", "ME": "153772"}, {"name": "ShettyInstituteofTechnologyGulbarga", "code": "E216", "AI": "92710", "CE": "171410", "CS": "62606", "EE": "114356"}, {"name": "MangaloreMarineCollegeandTechnology Mangalore", "code": "E219", "CS": "77820", "ME": "137304", "MR": "173275"}, {"name": "AllianceUniversityBangalore", "code": "E220"}, {"name": "AllianceUniversityBangalore", "code": "E220", "CE": "173905", "CS": "36881", "EC": "47831", "EE": "71422", "IG": "41618", "ME": "154589", "SE": "79607"}, {"name": "BiluruGurubasavaMahaswamijiInstituteofTechnologyMudhol", "AI": "91554", "CE": "155681", "CS": "62984", "EC": "77141", "ME": "167306"}, {"name": "CambridgeInstitututeofTechnology-NorthCampusDevanahalli(TQ)", "CS": "48391", "CY": "61369", "EC": "65262", "ME": "168600"}, {"name": "CauveryInstituteofTechnologyMandya tq", "code": "E227", "CE": "113609", "CS": "66981", "EC": "80769", "ME": "170595"}, {"name": "RevaUniversityBangalore", "code": "E232", "CE": "93044", "CI": "22041", "CS": "12510", "EC": "24094", "EE": "43477", "ES": "31343", "IB": "23070", "IE": "15836", "ME": "100891", "MT": "65179", "RO": "37978", "SS": "23512"}, {"name": "M.S.RamaiahUniversityofAppliedSciences Bangalore", "code": "E235"}, {"name": "M.S.RamaiahUniversityofAppliedSciences Bangalore", "code": "E235", "AI": "15702", "AT": "85177", "CE": "69538", "CS": "11515", "EC": "18662", "EE": "45446", "IE": "13312", "MC": "19333", "ME": "95261", "RB": "29679", "SE": "18828"}, {"name": "PresidencyUniversityYelahanka", "BD": "41122", "CA": "52020", "CE": "100483", "CG": "45457", "CO": "57395", "CS": "31458", "CY": "46797", "DS": "40838", "EC": "50376", "EE": "63810", "IE": "39334", "IO": "55953", "IS": "44749", "LC": "51871", "ME": "111990", "OP": "54706", "PL": "107752"}, {"name": "MysuruRoyalInstituteofTechnologyMandya (D)", "code": "E238", "CE": "160826", "CS": "55999", "EC": "66165"}, {"name": "EastWestCollegeofEngineeringYelahankaNewTown", "AE": "79310", "CS": "37649", "EA": "97502", "EC": "59242", "ME": "158908"}, {"name": "DayanandaSagarUniversityHosurRoad", "Le": "26347", "CG": "26994", "CS": "20208", "CY": "23916", "DS": "24304", "EC": "29545", "ME": "112814", "SE": "32370"}, {"name": "KLETechnologicalUniversity(FormerlyBVBCET)Dharward Dist", "code": "E241", "BT": "35048", "CE": "60862", "CF": "5512", "CS": "4145", "EC": "9856", "EE": "24153", "EV": "15127", "II": "15083", "ME": "61871", "RO": "24697"}, {"name": "MysoreCollegeofEngineeringandManagement  Mysore", "code": "E252", "Le": "62435", "CE": "170362", "CS": "49596", "DS": "64962", "EC": "59188", "IE": "55258", "ME": "156959"}, {"name": "AJInstituteOfEngineeringAndTechnology MANGALORE", "code": "E254", "CE": "146299", "CS": "28183", "EC": "58040", "IE": "40124", "ME": "165931"}, {"name": "GitamSchoolOfTechnologyBANGALORERURAL DIST", "code": "E255", "Le": "54726", "CB": "60674", "CE": "144387", "CS": "40283", "CY": "57548"}, {"name": "GitamSchoolOfTechnologyBANGALORERURAL DIST", "code": "E255", "DS": "53491", "EC": "65492", "EE": "81958", "IO": "62801", "ME": "174044"}, {"name": "CMRUniversityCHAGALATTI", "Le": "44677", "CS": "31455", "DS": "35096", "EC": "39870", "IG": "44341"}, {"name": "MaharajaInstituteofTechnologyTHANDAVAPURA", "AD": "112554", "CS": "25906", "EC": "44008", "ME": "141160"}, {"name": "NitteSchoolofArchitectureYELAHANKA BANGALORE", "code": "E260", "UP": "90736"}, {"name": "SchoolofPlanningandArchitecture  Mysore", "code": "E263", "LA": "146468"}, {"name": "JainCollegeofEngineeringandTechnology  Hubballi", "code": "E265", "CE": "172551", "CS": "34191", "EC": "40912", "ME": "173890"}, {"name": "JainCollegeofEngineeringandResearchUdyambhag", "CE": "148623", "CS": "36223", "EC": "44546", "ME": "169461"}, {"name": "GovernmentEngineeringCollegeTalakal", "CE": "173489", "CS": "47829", "EC": "78307", "EE": "90664", "ME": "172974"}, {"name": "GovernmentEngineeringCollegeViprasainagar"}, {"name": "GovernmentEngineeringCollegeViprasainagar", "CE": "172162", "CS": "58711", "EC": "83719", "EE": "118567", "ME": "154154"}, {"name": "GovernmentEngineeringCollegeMoselehosahalli", "CE": "174290", "CS": "43852", "EC": "65080", "EE": "85588", "ME": "172724"}, {"name": "RVInstituteofTechnologyandManagementJPNagar", "CS": "6613", "EC": "13286", "IE": "8332", "ME": "66428"}, {"name": "VisvesvarayaTechnologicalUniversityMuddenahalli", "MM": "99681"}, {"name": "VisvesvarayaTechnologicalUniversity  Belgaum", "code": "E279", "CB": "29155", "ES": "36616", "RA": "48454"}, {"name": "GovernmentEngineeringCollegeChallakere", "AI": "68793", "AU": "172761", "CS": "55756"}, {"name": "UniversityofMysoreMysore", "code": "E283", "AI": "45311", "BR": "63994", "CD": "47392", "CV": "131830"}, {"name": "SriJayachamarajendraCollegeofEngineering(Const.ofJSSUniv.)  Mysore", "code": "E284", "CS": "2954"}, {"name": "RVUniversityBangalore", "code": "E285"}, {"name": "RVUniversityBangalore", "code": "E285", "CS": "4726"}, {"name": "BGSCollegeofEngineeringandTechnologyMahalakshmipuram", "AI": "45286", "CD": "52293", "CS": "23398", "IE": "32843"}, {"name": "VidyashilpUniversityBangalore", "code": "E287", "DS": "63005"}, {"name": "GardenCityUniversityBangalore", "code": "E288", "DS": "72184", "IY": "83032", "RM": "89085"}, {"name": "VisvesvarayaTechnologicalUniversity-RegionalCenterRajapur", "CS": "38409", "ES": "76008"}, {"name": "VisvesvarayaTechnologicalUniversity-RegionalCenter  Mysore", "code": "E290", "CS": "17979"}, {"name": "GovernmentEngineeringCollegeNaragund", "AD": "95793", "CS": "62735"}]

def flatten_dict(original_dict) :
    new_dict = {}
    prefix = original_dict["name"] + " - "

    for key, value in original_dict.items():
        if key != "name":
            new_key = prefix + key
            new_dict[new_key] = value
    return new_dict

def flatten_keys(dictionary, parent_key='', sep='.'):
    flattened_dict = {}
    for key, value in dictionary.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_keys(value, new_key, sep=sep))
        else:
            flattened_dict[new_key] = value
    return flattened_dict


def create_one_dict(orig_dict) :
    appended_dict = {}

    for data in orig_dict:
        for key, value in data.items():
            if key in appended_dict:
                appended_dict[key].append(value)
            else:
                appended_dict[key] = value
    return appended_dict

flatten_clg_data = []
for index,clg in enumerate(clg_data) :
    flatten_clg_data.append(flatten_dict(clg))

the_dict = create_one_dict(flatten_clg_data)

#print(the_dict)

SeatMetrixDb.objects.all().delete()

"""
db = {}
for index, clg in enumerate(the_dict) :
    db[index] = SeatMetrixDb(info=clg)
    db[index].save()
"""

db = SeatMetrixDb(info=the_dict)
db.save()

fulldb = SeatMetrixDb.objects.all()

for a in fulldb :
    print(a.info)

