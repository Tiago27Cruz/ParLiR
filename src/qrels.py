from sklearn.model_selection import train_test_split
from ranx import Qrels

def split_queries_train_test(test_size=0.2, random_state=42):
    queries_map = get_queries_variations()
    in_numbers = list(queries_map.keys())

    metadata_ins = {1,2,10,12,13,15,16,17,18,21,22,23,24,28,29}
    labels = [1 if num in metadata_ins else 0 for num in in_numbers]

    train_ins, test_ins = train_test_split(
        in_numbers,
        test_size=test_size,
        random_state=random_state,
        stratify=labels
    )

    train_queries = {num: queries_map[num] for num in train_ins}
    test_queries  = {num: queries_map[num] for num in test_ins}
    
    return train_queries, test_queries


def get_correct_uris(query:int) -> set[str]:
    correct: set[str] = set()
    if query == 0:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_284015",
            "http://purl.org/polis/ar/initiatives#Initiative_284032",
            "http://purl.org/polis/ar/initiatives#Initiative_314948",
            "http://purl.org/polis/ar/initiatives#Initiative_304212",
            "http://purl.org/polis/ar/initiatives#Initiative_304233"
        }
    elif query == 1:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_263733",
            "http://purl.org/polis/ar/initiatives#Initiative_304155"
        }
    elif query == 2:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_314405",
            "http://purl.org/polis/ar/initiatives#Initiative_314907"
        }
    elif query ==3:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_263487",
            "http://purl.org/polis/ar/initiatives#Initiative_314817",
            "http://purl.org/polis/ar/initiatives#Initiative_263507",
            "http://purl.org/polis/ar/initiatives#Initiative_314617",
            "http://purl.org/polis/ar/initiatives#Initiative_284009",
            "http://purl.org/polis/ar/initiatives#Initiative_314631",
            "http://purl.org/polis/ar/initiatives#Initiative_263569",
            "http://purl.org/polis/ar/initiatives#Initiative_263632"
        }
    elif query ==4: # hab publica
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_263660",
            "http://purl.org/polis/ar/initiatives#Initiative_263745",
            "http://purl.org/polis/ar/initiatives#Initiative_263652",
            "http://purl.org/polis/ar/initiatives#Initiative_314802",
            "http://purl.org/polis/ar/initiatives#Initiative_273900"
        }
    elif query == 5: # defesa
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_314944",
            "http://purl.org/polis/ar/initiatives#Initiative_273900",
            "http://purl.org/polis/ar/initiatives#Initiative_263595",
            "http://purl.org/polis/ar/initiatives#Initiative_314943",
            "http://purl.org/polis/ar/initiatives#Initiative_304233",
            "http://purl.org/polis/ar/initiatives#Initiative_263566"
        }
    elif query == 6: # elevação a vila
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_294144",
            "http://purl.org/polis/ar/initiatives#Initiative_315024",
            "http://purl.org/polis/ar/initiatives#Initiative_315023",
            "http://purl.org/polis/ar/initiatives#Initiative_304228",
            "http://purl.org/polis/ar/initiatives#Initiative_294146",
            "http://purl.org/polis/ar/initiatives#Initiative_294145",
            "http://purl.org/polis/ar/initiatives#Initiative_263854",
            "http://purl.org/polis/ar/initiatives#Initiative_304227",
            "http://purl.org/polis/ar/initiatives#Initiative_263749",
            "http://purl.org/polis/ar/initiatives#Initiative_263750",
            "http://purl.org/polis/ar/initiatives#Initiative_294117"
        }

    elif query == 7: # abortos
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_314467",
            "http://purl.org/polis/ar/initiatives#Initiative_314476"
        }
    elif query == 8: # trans
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_283999",
            "http://purl.org/polis/ar/initiatives#Initiative_263752",
            "http://purl.org/polis/ar/initiatives#Initiative_304141"
        }
    elif query == 9: #feriados
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_263663"
        }
    elif query == 10:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_263515",
            "http://purl.org/polis/ar/initiatives#Initiative_263516",
            "http://purl.org/polis/ar/initiatives#Initiative_263517",
            "http://purl.org/polis/ar/initiatives#Initiative_263518",
            "http://purl.org/polis/ar/initiatives#Initiative_263519",
            "http://purl.org/polis/ar/initiatives#Initiative_263520",
            "http://purl.org/polis/ar/initiatives#Initiative_263521",
            "http://purl.org/polis/ar/initiatives#Initiative_263523",
            "http://purl.org/polis/ar/initiatives#Initiative_263524",
            "http://purl.org/polis/ar/initiatives#Initiative_263525",
            "http://purl.org/polis/ar/initiatives#Initiative_263526",
            "http://purl.org/polis/ar/initiatives#Initiative_263527",
            "http://purl.org/polis/ar/initiatives#Initiative_263528",
            "http://purl.org/polis/ar/initiatives#Initiative_263529",
            "http://purl.org/polis/ar/initiatives#Initiative_263530",
            "http://purl.org/polis/ar/initiatives#Initiative_263531",
            "http://purl.org/polis/ar/initiatives#Initiative_263532",
            "http://purl.org/polis/ar/initiatives#Initiative_263533",
            "http://purl.org/polis/ar/initiatives#Initiative_263534",
            "http://purl.org/polis/ar/initiatives#Initiative_263535",
            "http://purl.org/polis/ar/initiatives#Initiative_263536",
            "http://purl.org/polis/ar/initiatives#Initiative_263538",
            "http://purl.org/polis/ar/initiatives#Initiative_263545",
            "http://purl.org/polis/ar/initiatives#Initiative_263546",
            "http://purl.org/polis/ar/initiatives#Initiative_263558",
            "http://purl.org/polis/ar/initiatives#Initiative_263599",
            "http://purl.org/polis/ar/initiatives#Initiative_263605",
            "http://purl.org/polis/ar/initiatives#Initiative_263618",
            "http://purl.org/polis/ar/initiatives#Initiative_263626",
            "http://purl.org/polis/ar/initiatives#Initiative_263628",
            "http://purl.org/polis/ar/initiatives#Initiative_263641",
            "http://purl.org/polis/ar/initiatives#Initiative_263666",
            "http://purl.org/polis/ar/initiatives#Initiative_263715",
            "http://purl.org/polis/ar/initiatives#Initiative_263733",
            "http://purl.org/polis/ar/initiatives#Initiative_263735",
            "http://purl.org/polis/ar/initiatives#Initiative_263736",
            "http://purl.org/polis/ar/initiatives#Initiative_263737",
            "http://purl.org/polis/ar/initiatives#Initiative_263831",
            "http://purl.org/polis/ar/initiatives#Initiative_263850",
            "http://purl.org/polis/ar/initiatives#Initiative_263851",
            "http://purl.org/polis/ar/initiatives#Initiative_263853",
            "http://purl.org/polis/ar/initiatives#Initiative_263878",
            "http://purl.org/polis/ar/initiatives#Initiative_263879",
            "http://purl.org/polis/ar/initiatives#Initiative_273899",
            "http://purl.org/polis/ar/initiatives#Initiative_273967",
            "http://purl.org/polis/ar/initiatives#Initiative_283989",
            "http://purl.org/polis/ar/initiatives#Initiative_284038",
            "http://purl.org/polis/ar/initiatives#Initiative_284040",
            "http://purl.org/polis/ar/initiatives#Initiative_284089",
            "http://purl.org/polis/ar/initiatives#Initiative_294114",
            "http://purl.org/polis/ar/initiatives#Initiative_304155",
            "http://purl.org/polis/ar/initiatives#Initiative_304158",
            "http://purl.org/polis/ar/initiatives#Initiative_304216",
            "http://purl.org/polis/ar/initiatives#Initiative_304225",
            "http://purl.org/polis/ar/initiatives#Initiative_304231",
            "http://purl.org/polis/ar/initiatives#Initiative_304232",
            "http://purl.org/polis/ar/initiatives#Initiative_304317",
            "http://purl.org/polis/ar/initiatives#Initiative_304319",
            "http://purl.org/polis/ar/initiatives#Initiative_304328",
            "http://purl.org/polis/ar/initiatives#Initiative_304358",
            "http://purl.org/polis/ar/initiatives#Initiative_314423",
            "http://purl.org/polis/ar/initiatives#Initiative_314424",
            "http://purl.org/polis/ar/initiatives#Initiative_314425",
            "http://purl.org/polis/ar/initiatives#Initiative_314432",
            "http://purl.org/polis/ar/initiatives#Initiative_314488",
            "http://purl.org/polis/ar/initiatives#Initiative_314568",
            "http://purl.org/polis/ar/initiatives#Initiative_314579",
            "http://purl.org/polis/ar/initiatives#Initiative_314592",
            "http://purl.org/polis/ar/initiatives#Initiative_314595",
            "http://purl.org/polis/ar/initiatives#Initiative_314603",
            "http://purl.org/polis/ar/initiatives#Initiative_314662",
            "http://purl.org/polis/ar/initiatives#Initiative_314681",
            "http://purl.org/polis/ar/initiatives#Initiative_314689",
            "http://purl.org/polis/ar/initiatives#Initiative_314690",
            "http://purl.org/polis/ar/initiatives#Initiative_314691",
            "http://purl.org/polis/ar/initiatives#Initiative_314692",
            "http://purl.org/polis/ar/initiatives#Initiative_314693",
            "http://purl.org/polis/ar/initiatives#Initiative_314694",
            "http://purl.org/polis/ar/initiatives#Initiative_314711",
            "http://purl.org/polis/ar/initiatives#Initiative_314718",
            "http://purl.org/polis/ar/initiatives#Initiative_314719",
            "http://purl.org/polis/ar/initiatives#Initiative_314720",
            "http://purl.org/polis/ar/initiatives#Initiative_314731",
            "http://purl.org/polis/ar/initiatives#Initiative_314732",
            "http://purl.org/polis/ar/initiatives#Initiative_314737",
            "http://purl.org/polis/ar/initiatives#Initiative_314829",
            "http://purl.org/polis/ar/initiatives#Initiative_314879",
            "http://purl.org/polis/ar/initiatives#Initiative_314905",
            "http://purl.org/polis/ar/initiatives#Initiative_314906",
            "http://purl.org/polis/ar/initiatives#Initiative_315018",
            "http://purl.org/polis/ar/initiatives#Initiative_315019",
            "http://purl.org/polis/ar/initiatives#Initiative_315020",
            "http://purl.org/polis/ar/initiatives#Initiative_315021",

        }
    elif query == 11:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_263760",
        }
    elif query == 12:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_304286",
            "http://purl.org/polis/ar/initiatives#Initiative_273900",
            "http://purl.org/polis/ar/initiatives#Initiative_263785",
            "http://purl.org/polis/ar/initiatives#Initiative_314935",
            "http://purl.org/polis/ar/initiatives#Initiative_314574",
            "http://purl.org/polis/ar/initiatives#Initiative_314720",
            "http://purl.org/polis/ar/initiatives#Initiative_263551",
            "http://purl.org/polis/ar/initiatives#Initiative_284050",
            "http://purl.org/polis/ar/initiatives#Initiative_284061",
            "http://purl.org/polis/ar/initiatives#Initiative_314891",
            "http://purl.org/polis/ar/initiatives#Initiative_314628",
            "http://purl.org/polis/ar/initiatives#Initiative_304232",
            "http://purl.org/polis/ar/initiatives#Initiative_314687",
            "http://purl.org/polis/ar/initiatives#Initiative_263814",
            "http://purl.org/polis/ar/initiatives#Initiative_314650",
            "http://purl.org/polis/ar/initiatives#Initiative_263666",
            "http://purl.org/polis/ar/initiatives#Initiative_304165",
            "http://purl.org/polis/ar/initiatives#Initiative_314646",
            "http://purl.org/polis/ar/initiatives#Initiative_263801",
            "http://purl.org/polis/ar/initiatives#Initiative_304190",
            "http://purl.org/polis/ar/initiatives#Initiative_263799",
            "http://purl.org/polis/ar/initiatives#Initiative_314625",
            "http://purl.org/polis/ar/initiatives#Initiative_314883",
            "http://purl.org/polis/ar/initiatives#Initiative_314816",
            "http://purl.org/polis/ar/initiatives#Initiative_314790",
            "http://purl.org/polis/ar/initiatives#Initiative_304148",
            "http://purl.org/polis/ar/initiatives#Initiative_314864",
            "http://purl.org/polis/ar/initiatives#Initiative_263506",
            "http://purl.org/polis/ar/initiatives#Initiative_263838",
            "http://purl.org/polis/ar/initiatives#Initiative_294111"
        }
    elif query == 13:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_263563",
            "http://purl.org/polis/ar/initiatives#Initiative_263597",
            "http://purl.org/polis/ar/initiatives#Initiative_263618",
            "http://purl.org/polis/ar/initiatives#Initiative_263619",
            "http://purl.org/polis/ar/initiatives#Initiative_263821",
            "http://purl.org/polis/ar/initiatives#Initiative_263829",
            "http://purl.org/polis/ar/initiatives#Initiative_273956",
            "http://purl.org/polis/ar/initiatives#Initiative_273961",
            "http://purl.org/polis/ar/initiatives#Initiative_284019",
            "http://purl.org/polis/ar/initiatives#Initiative_284025",
            "http://purl.org/polis/ar/initiatives#Initiative_284085",
            "http://purl.org/polis/ar/initiatives#Initiative_304245",
            "http://purl.org/polis/ar/initiatives#Initiative_304258",
            "http://purl.org/polis/ar/initiatives#Initiative_304260",
            "http://purl.org/polis/ar/initiatives#Initiative_304307",
            "http://purl.org/polis/ar/initiatives#Initiative_304327",
            "http://purl.org/polis/ar/initiatives#Initiative_304374",
            "http://purl.org/polis/ar/initiatives#Initiative_314491",
            "http://purl.org/polis/ar/initiatives#Initiative_314850",
            "http://purl.org/polis/ar/initiatives#Initiative_315026"
        }
    elif query == 14:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_263742",
            "http://purl.org/polis/ar/initiatives#Initiative_263756",
            "http://purl.org/polis/ar/initiatives#Initiative_263508",
            "http://purl.org/polis/ar/initiatives#Initiative_263753",
            "http://purl.org/polis/ar/initiatives#Initiative_263535",
            "http://purl.org/polis/ar/initiatives#Initiative_273915",
            "http://purl.org/polis/ar/initiatives#Initiative_263737",
            "http://purl.org/polis/ar/initiatives#Initiative_263729",
            "http://purl.org/polis/ar/initiatives#Initiative_314989",
            "http://purl.org/polis/ar/initiatives#Initiative_294131",
            "http://purl.org/polis/ar/initiatives#Initiative_284087",
            "http://purl.org/polis/ar/initiatives#Initiative_273904",
            "http://purl.org/polis/ar/initiatives#Initiative_263747",
            "http://purl.org/polis/ar/initiatives#Initiative_263589",
            "http://purl.org/polis/ar/initiatives#Initiative_314550",
            "http://purl.org/polis/ar/initiatives#Initiative_314434",
            "http://purl.org/polis/ar/initiatives#Initiative_263574",
            "http://purl.org/polis/ar/initiatives#Initiative_263524",
            "http://purl.org/polis/ar/initiatives#Initiative_273912",
            "http://purl.org/polis/ar/initiatives#Initiative_304263",
            "http://purl.org/polis/ar/initiatives#Initiative_314620"
        }
    elif query == 15:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_263613",
            "http://purl.org/polis/ar/initiatives#Initiative_314509",
            "http://purl.org/polis/ar/initiatives#Initiative_284076",
            "http://purl.org/polis/ar/initiatives#Initiative_304233"
        }
    elif query == 16:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_314742",
            "http://purl.org/polis/ar/initiatives#Initiative_263567",
            "http://purl.org/polis/ar/initiatives#Initiative_314413",
            "http://purl.org/polis/ar/initiatives#Initiative_273917",
            "http://purl.org/polis/ar/initiatives#Initiative_314715"   
        }
    elif query == 17:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_263844",
            "http://purl.org/polis/ar/initiatives#Initiative_314689",
            "http://purl.org/polis/ar/initiatives#Initiative_304157",
            "http://purl.org/polis/ar/initiatives#Initiative_314426",
            "http://purl.org/polis/ar/initiatives#Initiative_314888",
            "http://purl.org/polis/ar/initiatives#Initiative_263804",
            "http://purl.org/polis/ar/initiatives#Initiative_263861"
        }
    elif query == 18:
        correct={
            "http://purl.org/polis/ar/initiatives#Initiative_314853",
            "http://purl.org/polis/ar/initiatives#Initiative_314744",
            "http://purl.org/polis/ar/initiatives#Initiative_314812",
            "http://purl.org/polis/ar/initiatives#Initiative_314813",
            "http://purl.org/polis/ar/initiatives#Initiative_314814"
        }
    elif query == 19:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_314779",
            "http://purl.org/polis/ar/initiatives#Initiative_314518",
            "http://purl.org/polis/ar/initiatives#Initiative_314750",
            "http://purl.org/polis/ar/initiatives#Initiative_263487",
            "http://purl.org/polis/ar/initiatives#Initiative_263507",
            "http://purl.org/polis/ar/initiatives#Initiative_284074",
            "http://purl.org/polis/ar/initiatives#Initiative_284048",
            "http://purl.org/polis/ar/initiatives#Initiative_263632",
            "http://purl.org/polis/ar/initiatives#Initiative_284070",
            "http://purl.org/polis/ar/initiatives#Initiative_314780",
            "http://purl.org/polis/ar/initiatives#Initiative_263583",
            "http://purl.org/polis/ar/initiatives#Initiative_314736",
            "http://purl.org/polis/ar/initiatives#Initiative_314784",
            "http://purl.org/polis/ar/initiatives#Initiative_314539"
        }
    elif query == 20:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_314923",
            "http://purl.org/polis/ar/initiatives#Initiative_314842",
            "http://purl.org/polis/ar/initiatives#Initiative_314914",
            "http://purl.org/polis/ar/initiatives#Initiative_314853",
            "http://purl.org/polis/ar/initiatives#Initiative_273900",
            "http://purl.org/polis/ar/initiatives#Initiative_314915",
            "http://purl.org/polis/ar/initiatives#Initiative_314845",
            "http://purl.org/polis/ar/initiatives#Initiative_314813",
            "http://purl.org/polis/ar/initiatives#Initiative_263518"

        }
    elif query ==21:
        correct = {
            "http://purl.org/polis/ar/initiatives#Initiative_263827"
        }
    elif query ==22:
        correct={
            "http://purl.org/polis/ar/initiatives#Initiative_263882"
        }
    elif query == 23:
        correct={
            "http://purl.org/polis/ar/initiatives#Initiative_263878",
            "http://purl.org/polis/ar/initiatives#Initiative_263883",
            "http://purl.org/polis/ar/initiatives#Initiative_263866",
            "http://purl.org/polis/ar/initiatives#Initiative_263888",
            "http://purl.org/polis/ar/initiatives#Initiative_263877",
            "http://purl.org/polis/ar/initiatives#Initiative_315017"
        }
    elif query == 24:
        correct={
            "http://purl.org/polis/ar/initiatives#Initiative_263497",
            "http://purl.org/polis/ar/initiatives#Initiative_263498",
            "http://purl.org/polis/ar/initiatives#Initiative_263501",
            "http://purl.org/polis/ar/initiatives#Initiative_263502",
            "http://purl.org/polis/ar/initiatives#Initiative_263503",
            "http://purl.org/polis/ar/initiatives#Initiative_263504",
            "http://purl.org/polis/ar/initiatives#Initiative_263551",
            "http://purl.org/polis/ar/initiatives#Initiative_263555",
            "http://purl.org/polis/ar/initiatives#Initiative_263556",
            "http://purl.org/polis/ar/initiatives#Initiative_263767",
            "http://purl.org/polis/ar/initiatives#Initiative_263774",
            "http://purl.org/polis/ar/initiatives#Initiative_263780",
            "http://purl.org/polis/ar/initiatives#Initiative_263791",
            "http://purl.org/polis/ar/initiatives#Initiative_263793",
            "http://purl.org/polis/ar/initiatives#Initiative_263795",
            "http://purl.org/polis/ar/initiatives#Initiative_263820",
            "http://purl.org/polis/ar/initiatives#Initiative_263843",
            "http://purl.org/polis/ar/initiatives#Initiative_263860",
            "http://purl.org/polis/ar/initiatives#Initiative_263886",
            "http://purl.org/polis/ar/initiatives#Initiative_263887",
            "http://purl.org/polis/ar/initiatives#Initiative_263888",
            "http://purl.org/polis/ar/initiatives#Initiative_273958",
            "http://purl.org/polis/ar/initiatives#Initiative_273973",
            "http://purl.org/polis/ar/initiatives#Initiative_273974",
            "http://purl.org/polis/ar/initiatives#Initiative_284003",
            "http://purl.org/polis/ar/initiatives#Initiative_284066",
            "http://purl.org/polis/ar/initiatives#Initiative_284069",
            "http://purl.org/polis/ar/initiatives#Initiative_284070",
            "http://purl.org/polis/ar/initiatives#Initiative_284071",
            "http://purl.org/polis/ar/initiatives#Initiative_294132",
            "http://purl.org/polis/ar/initiatives#Initiative_304143",
            "http://purl.org/polis/ar/initiatives#Initiative_304147",
            "http://purl.org/polis/ar/initiatives#Initiative_304183",
            "http://purl.org/polis/ar/initiatives#Initiative_304184",
            "http://purl.org/polis/ar/initiatives#Initiative_304185",
            "http://purl.org/polis/ar/initiatives#Initiative_304186",
            "http://purl.org/polis/ar/initiatives#Initiative_304211",
            "http://purl.org/polis/ar/initiatives#Initiative_304212",
            "http://purl.org/polis/ar/initiatives#Initiative_304213",
            "http://purl.org/polis/ar/initiatives#Initiative_304229",
            "http://purl.org/polis/ar/initiatives#Initiative_304230",
            "http://purl.org/polis/ar/initiatives#Initiative_304266",
            "http://purl.org/polis/ar/initiatives#Initiative_304315",
            "http://purl.org/polis/ar/initiatives#Initiative_304326",
            "http://purl.org/polis/ar/initiatives#Initiative_304333",
            "http://purl.org/polis/ar/initiatives#Initiative_304335",
            "http://purl.org/polis/ar/initiatives#Initiative_304336",
            "http://purl.org/polis/ar/initiatives#Initiative_304337",
            "http://purl.org/polis/ar/initiatives#Initiative_304391",
            "http://purl.org/polis/ar/initiatives#Initiative_314440",
            "http://purl.org/polis/ar/initiatives#Initiative_314633",
            "http://purl.org/polis/ar/initiatives#Initiative_314649",
            "http://purl.org/polis/ar/initiatives#Initiative_314650",
            "http://purl.org/polis/ar/initiatives#Initiative_314721",
            "http://purl.org/polis/ar/initiatives#Initiative_314779",
            "http://purl.org/polis/ar/initiatives#Initiative_314780",
            "http://purl.org/polis/ar/initiatives#Initiative_314781",
            "http://purl.org/polis/ar/initiatives#Initiative_314798",
            "http://purl.org/polis/ar/initiatives#Initiative_314802",
            "http://purl.org/polis/ar/initiatives#Initiative_314851",
            "http://purl.org/polis/ar/initiatives#Initiative_314858",
            "http://purl.org/polis/ar/initiatives#Initiative_314863",
            "http://purl.org/polis/ar/initiatives#Initiative_314877",
            "http://purl.org/polis/ar/initiatives#Initiative_314887",
            "http://purl.org/polis/ar/initiatives#Initiative_314954",
            "http://purl.org/polis/ar/initiatives#Initiative_314966",
            "http://purl.org/polis/ar/initiatives#Initiative_315004",
            "http://purl.org/polis/ar/initiatives#Initiative_315016",
            "http://purl.org/polis/ar/initiatives#Initiative_315017"
        }
    elif query == 25:
        correct={
            "http://purl.org/polis/ar/initiatives#Initiative_304154",
            "http://purl.org/polis/ar/initiatives#Initiative_294131",
            "http://purl.org/polis/ar/initiatives#Initiative_294099",
            "http://purl.org/polis/ar/initiatives#Initiative_304153",
            "http://purl.org/polis/ar/initiatives#Initiative_304144",
            "http://purl.org/polis/ar/initiatives#Initiative_304313",
            "http://purl.org/polis/ar/initiatives#Initiative_304142",
            "http://purl.org/polis/ar/initiatives#Initiative_294100",
            "http://purl.org/polis/ar/initiatives#Initiative_294102",
            "http://purl.org/polis/ar/initiatives#Initiative_304147",
            "http://purl.org/polis/ar/initiatives#Initiative_314872",
            "http://purl.org/polis/ar/initiatives#Initiative_294101",
            "http://purl.org/polis/ar/initiatives#Initiative_304189",
            "http://purl.org/polis/ar/initiatives#Initiative_314889",
            "http://purl.org/polis/ar/initiatives#Initiative_304172",
            "http://purl.org/polis/ar/initiatives#Initiative_294103"
        }
    elif query == 26:
        correct={
            "http://purl.org/polis/ar/initiatives#Initiative_304148",
            "http://purl.org/polis/ar/initiatives#Initiative_314881",
            "http://purl.org/polis/ar/initiatives#Initiative_314869",
            "http://purl.org/polis/ar/initiatives#Initiative_314862",
            "http://purl.org/polis/ar/initiatives#Initiative_304264"
        }
    elif query == 27:
        correct={
            "http://purl.org/polis/ar/initiatives#Initiative_314488",
            "http://purl.org/polis/ar/initiatives#Initiative_304182",
            "http://purl.org/polis/ar/initiatives#Initiative_304185",
            "http://purl.org/polis/ar/initiatives#Initiative_304201",
            "http://purl.org/polis/ar/initiatives#Initiative_314905",
            "http://purl.org/polis/ar/initiatives#Initiative_283985",
            "http://purl.org/polis/ar/initiatives#Initiative_294107",
            "http://purl.org/polis/ar/initiatives#Initiative_314797",
            "http://purl.org/polis/ar/initiatives#Initiative_283989"
        }
    elif query == 28:
        correct={
            "http://purl.org/polis/ar/initiatives#Initiative_273904"
        }
    elif query == 29:
        correct={
            "http://purl.org/polis/ar/initiatives#Initiative_263813",
            "http://purl.org/polis/ar/initiatives#Initiative_284049"
        }
    return correct

def get_queries_variations():
    return {
        0: [
            "congelar, reduzir ou abolir propinas universitárias",
            "diminuir ou manter custo propinas faculdade",
            "baixar ou congelar propinas do ensino superior",
            "conglar, redozir ou abulir propias universitarias"
        ],
        1: [
            "Inquéritos parlamentares realizados pela IL",
            "inqueritos parlamentares da iniciativa liberal",
            "IL inquéritos parlamentares",
            "iniciativa liberal inquerios parlamentars"
        ],
        2: [
            "decreto de lei 33/2022",
            "decreto-lei 33/2022",
            "incativas sbore o decreto    de lei 33 2022",
            "decreto lei 33 2022 iniciativas"
        ],
        3:["dedicação exclusiva ao SNS",
           "SNS dedicação exclusiva proposta",
           "sns exclusividade profissionais",
           "dedicaçao exclusiva sns"
        ],
        4:[
            "aumento da oferta de habitação pública",
            "construção de habitação pública",
            "medidas para aumentar habitação publica",
            "habitação do estado aumentar oferta"
        ],
        5:["investimento na defesa",
           "despesa militar aumentar",
           "defesa nacional investimento",
           "investimnto defesa"
        ],
        6:[    "propostas para tornar povoações em vilas",
                "elevar povoações a vilas",
            "novas vilas portugal propostas",
            "tornar vila povoacoes"
        ],
        7:["aumentar o número de semanas que se pode abortar",
            "alargar prazo legal do aborto",
            "IVG prazo aumentar",
            "aumntar semanas aborto"
        ],
        8:["medidas de proteção a pessoas trans",
            "direitos e proteção de pessoas trans",
            "segurança e direitos trans",
            "pessoas trans proteçao"],
        9:["adicionar novo feriado",
            "criar um novo feriado nacional",
            "proposta de novo feriado",
            "adiconar feriado"
        ],
        10:["Iniciativas do Rui Rocha", "Rui Rocha autor", "Iniciativas escritas pelo Rui Rocha", "Inicativas do rui riocha"],
        11:["Propostas que mencionem o Cavaco Silva negativamente", "Menção negativa ao cavaco silva", "Cavaco Silva menção negativa", "Menç~oesnegatives a cavaco silva"],
        12:["Educação", "Educaçao", "educaçºao", "Propostas a cerca da Educação"],
        13:["Projetos de Deliberação", "Projetos de deliberaçao", "projetos deliberação", "projetos deliveração"],
        14:["Redução do IVA", "iva reduzir", "redzir iva", "baixar o Imposto sobre o Valor Acrescentado"],
        15:["Iniciativas que mencionem Tomar", "Tomar  menções", "Tomar cidade", "menciona Tomar"],
        16:["Propostas do PSD sobre saúde", "PSD saúde", "saude PSD", "PSD-PPD saúde"],
        17:["Projetos de Lei sobre imigração", "imigração projetos de lei", "projeto lei imigração", "projeto de lei imgraçao imigrantes"],
        18:["Propostas do Chega sobre corrupção", "Chega corrupção", "corrupção Chega",  "chega curupção"],
        19:["reduzir listas de espera no SNS", "listas de espera SNS baixar", "redução das listas de espera no sns", "reduzir listas espera no sistema nacional saude"],
        20:["inteligência artificial", "inteligencia artificial", "IA", "intelgência artificial"],
        21:["propostas do PCP sobre transporte público no Rio Sado", "PCP transporte público Rio Sado", "pcp rio sado transporte", "Rio Saado transporte PCP"],
        22:["Projetos de lei do PAN para limitar voos", "PAN limitar voos Projetos de lei", "limitar voos PAN Projetos de lei", "limitar vôos pan projeto de lei"],
        23:["plano ferroviário nacional", "menções ao plano ferroviário", "plano ferroviario nacional", "plano feroviario nacional"],
        24:["Projetos de Resolução autorados pela Marisa Matias", "Marisa Matias projetos de resolução", "projetos resolução da Marisa Matias", "Marisa Matias autora proijeto resolição"],
        25:["medidas para os incêndios", "incêndios", "medidas sobre incêndios", "incendios"],
        26:["Criar carreiras na área da educação", "criar carreiras na educação", "novas carreiras educação", "careiras na educaçao"],
        27:["Iniciativas sobre a venezuela", "Venezuela", "iniciativas Venezuela", "venezoela"],
        28:["Mencione a lei 55/2012 e a lei 16/2001", "lei 55/2012 e lei 16/2001", "leis 55/2012 16/2001", "lei nº 55/2012 lei nº 16/2001"],
        29:["Menciona a Portaria 426/2023", "Portaria 426/2023", "menções à portaria 426/2023", "Portaria426/2023"]
    }

def build_trec_topics(needs: dict[int, list[str]]) -> str:
    blocks = []
    for iid, variants in needs.items():
        for vidx, query in enumerate(variants):
            qid = f"{iid}-{vidx}"
            blocks.append(
                f"<top>\n<num>{qid}</num> \n\n <title>{query}</title> \n\n <desc>\n\n </desc> \n\n <narr>\n\n </narr>\n</top>"
            )
    return "\n\n".join(blocks)

def create_dataset():
    qrels_dict = {}

    query_vars = get_queries_variations()
    #topics = build_trec_topics(query_vars)
    #with open("out/queries/topics.xml", "w", encoding="utf-8") as f:
    #    f.write(topics)

    for num, queries in query_vars.items():
        correct = get_correct_uris(num)
        correct_dict = {}

        for uri in correct:
            correct_dict[uri] = 1


        for i, q in enumerate(queries):
            qrels_dict[f"{num}-{i}"] = correct_dict

    qrels = Qrels(qrels_dict)
    
    qrels.save("out/qrels_complete.json")
    qrels.save("out/qrels_complete.trec") 
    with open("out/qrels_complete.trec", "r", encoding="cp1252") as f:
        content = f.read()
    with open("out/qrels_complete.trec", "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    qrels.save("out/qrels_complete.parquet")

    train, test = split_queries_train_test()
    qrels_dict = {}
    for num, queries in train.items():
        correct = get_correct_uris(num)
        correct_dict = {}

        for uri in correct:
            correct_dict[uri] = 1


        for i, q in enumerate(queries):
            qrels_dict[f"{num}-{i}"] = correct_dict

    qrels = Qrels(qrels_dict)
    qrels.save("out/qrels_train.json")
    qrels.save("out/qrels_train.trec") 
    with open("out/qrels_train.trec", "r", encoding="cp1252") as f:
        content = f.read()
    with open("out/qrels_train.trec", "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    qrels.save("out/qrels_train.parquet")

    qrels_dict = {}
    for num, queries in test.items():
        correct = get_correct_uris(num)
        correct_dict = {}

        for uri in correct:
            correct_dict[uri] = 1

        for i, q in enumerate(queries):
            qrels_dict[f"{num}-{i}"] = correct_dict

    qrels = Qrels(qrels_dict)
    qrels.save("out/qrels_test.json")
    qrels.save("out/qrels_test.trec") 
    with open("out/qrels_test.trec", "r", encoding="cp1252") as f:
        content = f.read()
    with open("out/qrels_test.trec", "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    qrels.save("out/qrels_test.parquet")
            
from statistics import median
def get_median_correct_per_IN():
    counts = [len(get_correct_uris(i)) for i in range(30)]
    print(median(counts))


if __name__ == "__main__":
    get_median_correct_per_IN()