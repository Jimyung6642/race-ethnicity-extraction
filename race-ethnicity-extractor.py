from collections import defaultdict
import regex as re
import pandas as pd
import os
import csv

def regex():

    path = "C:/Users/bzeli/OneDrive/Desktop/Sci_Re/CODING/download/"
    files = os.listdir(path + "2000txtfiles")   

    race_matches = {}
    races = []
    csvFile=open(path+"2000masterracedoc.csv",'w',newline='')
    writer = csv.writer(csvFile)

    for i in range(0,len(files)):
        list = []
        file= files[i]
        file_path = path + "2000txtfiles/" + file
        print(file_path)
        f = open(file_path, "r", encoding="UTF-8")
        file_content = ' '.join([line for line in f])
        race_matches[file_path] = defaultdict(int)

        races_terms = 'latino|latina|latinx|pashtun|hispanic|tajik|hazara|uzbek|aimaks|turkmen|baloch|albanian|greeks|vlachs|gypsies|serbs|bulgarians|arabberber|andorran|portuguese|french|ovimbundu|kimbundu|bakongo|mestico|european|black|british|portuguese|lebanese|syrian|white|mestizo|amerindian|armenian|russian|kurds|caucasian|asian|aboriginal|croatians|slovenes|serbs|bosniaks|turks|german|azeri|dagestani|russian|armenian|armenians|nagornokarabakh region|black|white|bahraini|nonbahraini bengali|nonbengali muslims black|white|belorussian|russian|polish|ukrainian|fleming|walloon|creole|chinese|indigenous|bulgarian|turk|romamacedonian|armenian|tatar|circassian|fulani hutu|bantu|tutsi|hamitic|pygmy| khmer|vietnamese|chinese|cameroon highlanders|equatorial bantu|kirdi|fulani|northwest bantu|eastern nigritic|african|indigenous indian and inuit|asian|african|arab |mulatto|african|european baya|banda|mandjia|mboum|mbaka|yakoma|arabs|gorane|toubou|kreda|zaghawa|kanembou|ouaddai|baguirmi|hadjerai|fulbe|kotoko|hausa|boulala|sara |ngambaye|mbaye|goulaye|moundang|moussei|massa white and whiteamerindian|amerindian|han chinese|zhuang|uygur|tibetan|manchu|mongol|buyi|korean|white|mulatto|black|blackamerindian|cafre|makoa|oimatsaha|bantu|mongo|luba|kongo|bantu|mangbetuazande|hamitic|kongo|sangha|mbochi|europeans and white |including mestizo|black|amerindian|chinese|voltaiques|northern mandes|krous|southern mandes|lebanese|french|croat|serb|bosniak|hungarian|slovene|czech|romanian|albanian|montenegrin|white|black|chinese greek|turkish |czech|moravian|slovak|scandinavian|inuit|faroese|german|turkish|iranian|somali somali|afar |french|arab |ethiopian|italian black|black and european|european|syrian|carib amerindian white|black|austronesian |malayopolynesian|papuan|small chinese minority mestizo |amerindian and white|amerindians|black egyptian|berber|nubian|bedouin|beja|greek|armenian|european |primarily italian and french| mestizo|white|amerindian bioko|europeans|tigre and kunama|estonian|russian|ukrainian|belorussian|finn |oromo|amhara and tigrean|sidamo|shankella|somali|afar |gurage|fijian|indian|european|pacific islanders|overseas chinese|and finn|swede|sami |lapp |romanian|estonian celtic and latin with teutonic|slavic|north african|southeast asian|nzeiby|mbede|obamba|bateke|africans and europeans|mandinka|fula|wolof|jola|serahuli|nonafrican georgian|azeri|armenian|russian|german|turkish|italian|greek|polish|black african|akan|moshidagomba|gurma|yoruba european and greek|black and european|european and east indian arawak|carib amerindian mestizo|ladino|amerindianspanish ancestry|kiche|kaqchikel|qeqchi|mayan|indigenous nonmayan|peuhl|malinke|balanta|manjaca|mandinga|black|amerindian|white|chinese|mulatto and white mestizo|amerindian|black|white hungarian|indoaryan|dravidian|mongoloid and javanese|sundanese|madurese|coastal malays|persian|azerbaijani|kurd|arab |baloch|turkmen|arab |kurdish|turkoman|assyrian|celtic|europe|americas|oceania born|israel born|africa born|asia born|non jewish|italian|french|black|east indian|white|chinese|japanese|korean|chinese|brazillian|filipino|arab |circassian|armenian kazak |qazaq|russian|ukrainian|uzbek|german|tatar|uygur|african|asian|european|kuwaiti|arab |south asian|iranian|kyrgyz|uzbek|russian|dungan|ukrainian|uygur|lao loum|lao theung|lao soung|hmong|mien|ethnic vietnamese|chinese latvian|russian|belorussian|ukrainian|polish|lithuanian|arab |armenian|sotho|europeans|asians|greeks|maltese|italians|egyptians|pakistanis|turks|indians|tunisians alemannic|italian|turkish|lithuanian|polish|russian|portuguese|italian|slavs |montenegro|albania|kosovo|macedonian|albanian|turkish|romaniangypsy|serb|malayoindonesian |merina and related betsileo|african|malayoindonesian|arab ancestry|betsimisaraka|tsimihety|antaisaka|sakalava|french|indian|creole|comoran chewa|nyanja|tumbuko|yao|lomwe|sena|tonga|ngoni|ngonde|asian|european malay|chinese|indigenous|indian|south indians|sinhalese|arabs mande |bambara|malinke|sarakole|peul|voltaic|tuareg and moor|songhai|maltese |descendants of ancient carthaginians and phoenicians| micronesian maur|black|maur|black indomauritian|creole|sinomauritian|francomauritian mestizo |amerindianspanish|amerindian or predominantly amerindian|white|moldavian|romanian|ukrainian|russian|gagauz|bulgarian|french|monegasque|italian|mongol |khalkha|turkic|montenegrin|serbian|bosniak|albanian|muslims|croats|romanian| arabberber|jewish|shangaan|chokwe|manyika|sena|makua|europeans|euroafricans|indians burman|karen|rakhine|chinese|indian|black|white|ovambo tribe|kavangos tribe|herero|damara|nama|caprivian|bushmen|baster|tswana nauruan|pacific islander|chinese|european brahmanhill|chetri|tamang|newar|muslimi|yadavs|moroccans|antilleans|surinamese|european|maori|pacific islander|asian|unspecified mestizo|white|black|amerindian hausa|djerma|tuareg|beri beri |kanouri|arab |toubou|gourmantche|yoruba|south asian|indian|pakistani|sri lankan|bangladeshi|african punjabi|sindhi|pathan|baloch|muhajir|palauan|filipino|chinese|asian|white|carolinian|micronesian|jewish |gaza strip|jewish mestizo|amerindian|west indian|white|indian melanesian|papuan|negrito|micronesian|polynesian mestizo amerindian|mestizo|white|black|japanese|chinese|tagalog|cebuano|ilocano|bisaya|binisaya|hiligaynon ilonggo|bikol|waray|polish|german|belorussian ukrainian|pakistani|indian|iranian|romanian|hungarian|romanian|gyspy|ukrainian|german|russian|turkish'
        # patient_terms = 'girl|boy|patient|american|child|children|participants|girls|boys|patients|americans|male|males|female|females|participant|woman|women|man|men|subject|subjects|mother|mothers|father|fathers|volunteer|ancestry|ancestries|descent|descendants|descendant'
        # pattern = f'({races_terms})([\w\s]+?)\\b({patient_terms})\\b'
        pattern = f'({races_terms})([\w\s]'+'{,20})\\b(girl|boy|patient|american|child|children|participants|girls|boys|patients|americans|male|males|female|females|participant|woman|women|man|men|subject|subjects|mother|mothers|father|fathers|volunteer|ancestry|ancestries|descent|descendants|descendant)\\b'
       
        matches = re.findall(pattern, file_content.lower())
    # print(matches)

        list.append(str(file))

        for match in matches:
            print(''.join(match))
            print(match)
            list.append(matches)

        writer.writerow(list)
    
regex()
