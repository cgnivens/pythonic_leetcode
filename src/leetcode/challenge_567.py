# https://leetcode.com/problems/permutation-in-string/


from itertools import permutations
from collections import Counter
from typing import Iterator

class Solution:
    def string_chunk(self, s: str, N: int) -> Iterator[str]:
        for a, b in zip(range(len(s) - N + 1), range(N, len(s) + 1)):
            yield ''.join(sorted(s[a:b]))


    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Checks if a permutation of s1 is present in s2.

        First, check if s1 is a subset of s2. If it isn't, short-circuit.
        Next, we sort s1 and then generate N-length substrings from s2. We
        sort the substrings. If there is a match, then s1 is included in s2
        """

        c1, c2 = Counter(s1), Counter(s2)
        for letter, count in c1.items():
            if c2.get(letter, 0) < count:
                return False

        N = len(s1)
        sorted_s1 = ''.join(sorted(s1))

        # need to generate chunks of letters that are
        # N letters long
        for substr in self.string_chunk(s2, N):
            if substr == sorted_s1:
                return True

        return False


def run_tests():
    s = Solution()
    n = len(tests)

    for i, (s1, s2, result) in enumerate(tests, start=1):
        try:
            assert s.checkInclusion(s1, s2) is result
        except:
            raise RuntimeError(
                f"Bad result for the test case {i}:"
                "\n"
                f" s1: {s1}"
                "\n"
                f" s2: {s2}"
                "\n"
                f"Expected {result} but got {not result}"
            )
        else:
            print(f"Passed case {i} of {n}")

    print('All test cases passed')


tests = [
    ("ab", "eidbaooo", True),
    ("dinitrophenylhydrazine", "acetylphenylhydrazine", False),
    ("xuumbjffxuzovdwrnolopeingppzgorotzdqfprokkmucxwsub", "jpdojwinknmyeorfdhpsysyealozhgbapagzjsivbxmcyijlbdafupblrawguoazuzcqupobxayrkpqxawytdsdznljnxulaugewrbjmkslsrllixpkuvorhnnhkzikovsajrbhjdybocvjloqiikidsnwcubhliajwwqkpqaugidhfxqfxrkluvadcdmekdhckszpojvwpiquazmaecaxxwsnswzxbctqeqhjsrgnjsjmaqbexexuwgfglixsthifevokdgexxkdmzaxrcilmthzemuomexwzipzivdyxqnvgzpjavonrkobmgkormdmfiwwalgdzwlngkrjmdwkknajqatghoddybqfkorhpmrkfcfwsaproaenfedvfendprnlpmuqklsqrsjuejyxulfuhdsyolthhhfhmxorojnjsvqyworupkdzhyqkzikvhltfsrhrecmyyddtinphjsmmbdtrouyifvsvvlamwhkffrrywdiawpvxwcwfkcunbjaelbcmdwczikkfelahowtbwqbdcjggnmknfhjdtusfjotsbjgtlnuonlxjlcwyqiffktonvtrkcogosfbcvcosktnvbeitxuqpexxejnklndzbtzlzeebwufoiwqqcoemnshcpovntjgidophekyntcsrwzvovwmostqudxgeaowehcmqmdrllovmmbgqhaxrqluizhhhslystwkhckjtosnomfvyibkasycxnnmvkbwkbhzeayezughsmqovogrnihjgetsdvhymjmnijzwvpasurcaybmyzfbqepjsdqwmkmomzkociaqtnkwiguylhwxrfamyxjvfxwonwblidvcsenvwigjjqdsnnydlgdhlsdtonvuapzaozkdtyiartimmpwgotnwpiwimbdunqfickerusbvrqwazvnwgdczvnqtigjmkjgsridfulxjekazzqkdynyuutyoffhntfbcruhrmnhhjyyzfszbaqykgnroepiovqqlhdtkizvpivukdutitwzhapvcyfghqvtjyyrdbctvdccoxjtsovdosbyqaiffumnrfokrbgvedxbcytvbcaeoviutdmxwfhxgchnusazcztitxgyjrkjdmajbndlemsnpjwzgvpitrfrjoxivhisgkzncmkewphusvaycteennpltuevohegzvafwxuebmovgkpwlgyoutsbbgxoxdzyisersgaqcnnjnjtjwufqscjzccudbkdcnmorpmraqapvirijlpretmezlrbdvnfixvmalzmgrhwpkhisaztpsgvlooqxezzscjrtnmmctoyinjermwrrmjlfbizryripnarkvnabdizzereczdnbkojpfmxhlfvlztmzpskwttzyusxaudprxpbpihorlipzpdiucpvrqlscmoipvdzsrowjrwmxzomtcxxehrmcaxmtifcvftywjkzgdsohvomcthhylzpijujfyysbientozyirurugevubxpdpbihrudvgdmhwyxuhyorvufffqzifwzszmfswhkesywfyozffzarrklnxppymoaslqctlfbtrykccmgmhrdacuelfrbflsjxhdagaevscxerljtxnwodtfioyxjoaxyhzjmttvflfhqvvcbwvmnulcsubtwngjvomqkqrjtntkzuclolcjmiypjilgvezphjqrjetqnaccrjmxydmmkbmuyxwotfynptdotuaxpxzgjulwgwfbprzolxablskvidnmnzcofemsodetsiubqrvtbkshuokkuomjezwbmtcjvapnlsmutehyfxaqjqlibfzitcfhuivmmclulnrwyknbymyfcwbgyxtavcaebvfwlkikylkrpcfappcamnjenpggoxcrpxdbqjqzrdvnfzxuxuaixbpiqmitzhefcgyhzayemxgrtdoiryqguiexsrysetobkqnfphdechsgoqvmdhurzhvflsbxsdjemmvlzpthrjizfcayxemztvszhhpfvvjgoejrjnmyvxstpejfmiukuocmrgvinqifpdcqvwfddoiyopbzverxwcqdyoqzeqcjcwmojbhcnrksebanfpdhhpiaguxracnxzttbjgruczuhwwjbmznzgdijyemrwcawodqftjtlyozqwwchxtlvlnjqwklmbzirfhaquiltdijijeglroopaagmyrkhqbnkhbxvguodmmszfoomhfvwjsnrmmzjuyxhotehlezyyiptzububvazwzziskqagtpthflchvvanpugjpeoipecmvgkocylsqduwbreeifhjdomajmnbwrmxuhvvjnfblyvtveqalkqlbxkxvmxfefvijptnpvhmgmotrvsxmarhkspdlybniuoxycahgisvnrlrukendhsxvvcqzinnbkryzwbnktsgfwxjklrcgvtrzvkqfbhctljoijsvxbnwiunrasctvuetwvzdulmlnxeivsvujihlmjroxntmgkecjkimcsvfesfeursbuchaexgpyqakllumehlfdkuzbnulwfdacxjalozmrneqtjvdpgkcwnrkuhhqbnpedmysjqcrdqaawiwcucuzlbkwozlgrgcroyebklrwzkqicuqezkswayknmcytcsrtkxkfwxmimpolrqzjwfdzmlkpinifykobpvqlzqrcliorfqygytfgpdociwflhwpuuumrwnhrkpnteqacxejyulkccgxtnsfhuuahifvsshkwrkhptqvcmylyvvykwjhgknmsuolomginxdfwvqpfwlpwvommjjymsunxmbjxlcznmefzvuckeqfpighnxzxdpdlcifxbzldjctrswxmrxcjbbtivfnwqelhkmbunsroodysywhjsysajsrngtsvimguuwaicmuqzmafocvdzudgkmmvhydmafxqrrpkvvnnjyzohjwtjgqbrptggknxpuatfycatgimywhbafhjazjklgzxaiecmqbqgwgdepfspuxakrowawfolujdcyqsmakrkiqiduitooygdduztcquxqyraxhwjkvybbyiksqyqxqfmyzjyxxrxktmfklcjsjeijjflvtjayqlfuqtacxrfbrsdqtuwmflpdtxtjezsgeoeeyhcpncbknslbexvicfxslnqbelcfjonoakbitkizdlmusmydyajmiiouvqhhpmjspwoprvajocrloqydqbrgzxqafbfonuvecxjcrpoiorfqxofionzmomccxkhjqzkvpdevkwpsikonjxfthvtorexdyntvhttbtygzmtrrzprsgqnvbzhxuiruhugtaogfrjqdxnilxatjyltpbchjlkajaxefdjjwhqzjeejznbjkhdjqoltccfgosuuxodgyhvufwdrdxtpuvxlthxibekzkdoufkbstuxhwukrfaqsbratipaaxjawndpognykgltxofqbypomdpdsgncggpoddzbobloikifupdfgytydhxoxtcyerqpgezsddndikvcwufcefpdkdgvrlmvoiadawofsuyezliebpixyqboteavtvqeojxmemrdbptsxdckszxjgveaqngboxfdxqdgddczdzpyhlztthvbzgutaioqswwpzupddayzktwvqyvxcflmolxyewseqrrvpovpeftwgiywoyflwejpffxpubejlwmazjzfcldadgnkkjtmxktuzlocvqhjajqrfrfaloychnmokakwsfkrtacwjgsieptnujtgbbwzllvkpeuewegmkchhaaaptmbmoybtdotctkfyumafregkthibmufiudjrcohdhuhlpjeishhekicdfiiostjmofwhreoegrnbqgkhmiezgtasdaqdcixsrdfdsfcrgjaryeqtkussultserwmyealuvxckhcgojsxzsfxmrtcfhqpowalbbzvpcltiwdhexbvcjojdptxeplgestsnpmpibymzaolqaybmeezyagvvftcuqgqrpjauxjnmudeasbpeormqofrbmmgorysyztkbloyfjikxdrytsdfdrjagghbbjqkujemzvvtioluzitrmaxjphducstlearfirqknijfdurdztizvwoeqzamxkbbvmnbxomhsxfmwdhocdyabcygzojqebxferyieqfislcpwiaadbarnsgnuvhkaidexxcgxhmvsiwqhoxkjwvycbyaqiddlrgsvqvzkvqzeewbxnfqlhavmqyucnnlskzyhwlnpglakbstcsnmsipeekjbwvokjjasfcruinzkcmjtkuztnglqakavnjmvccjgquzfftcqzwnrvywoqxhzbkbjufjuyqqqtaoakzbykeraqalcqzuhjndgusnvdanqrwemqsmcwxelogrfxxsdyzlbfuvopxsyzuizshrtauculajiapoentvnkxpvyfxfecjolvlezsmfmibhptmgdkiucnsralqhtutgvnpzicjwcgrtcgyueuqsxnyspxmnzhupjwalphkutczrptfxsvgeikwqqhesezmkoliizhceciotrcrjhunyfnpeyrnmucyhkozbipsmuqfgujshzhzuxextaapmrbhvexaqyifwrodhftkwbpyndylvfukebddabmjperimjtzeeqwmjzjxjrqglwcsuxinztzxpzfdlirmyroecjkimmgnybedfhssjfzzdnqlzihfgobikowitiqdyzlhxbxifamfkeienxqvcmvhzixicqlylurlfnzbrfoztfjxswwlxkvrhueccohddaazuluirluhzliuqeqiajvmvtbpibfhiulyagqfowibqjkjewqminwsuupmxnijyrbiodfknndgpfiannwlkillxmirfqmmoktexmoqxqujogmxjmkenfphffmdfablsaqxufjwvmufogrzjarlopjhidbfbhoivkknzgqresjprfknjetohwtqurxyngxilywmbgpsctswswwkasyisochqeslbiunnbgxsgzwkopnhgdjyuherwtrkypbjrdesztgkxzueqrhhicwndmidmqahdwcycqpgtuildbowqhjaqnmblbnvvsxahycecvfnbvqzcjburykyjkgazgauobvieoerphnehdjxfianvcaasrctenrcwcgzcqbzufwsqllzbxnjzktgermrodlzuvkdblqcwbfjevjkygbgoalqyibexruhsxsowmchcogiffedbuddithpwocmovwbpvxzhwmyzpuwdhrorlqxxtqtwswmdcszbxwyirhpwjjulqoovmgqydxctjrnncsfevitouvdvsgdftpyjztxrxhuggdtyfandnuvufixthdxidrlzzkssngvrmtkwzifwjoqyawcohqxrucjixdcrhgybujxpbjfwxunbbotjlijfagrdsbeemkvgaebuagweegcgpoleicaakefhgvgjislsamatuqmmjisifffwmigqwxaywwmoyzarwtpiimekzofbycyoqznbnqwnncmzoiwpjgpymvynrgasxpekunmzksdrfxlyxewqmfoeufccrwevhhxxjqzkptkctaqerwotatqgkbnjqbpfyglucttnmxpxrrjhglbmzzjtyupaexfismwrvfgtunlriabhhyklpmevgmltnkdttjmemegytzzikcykidlasvugyzfaozknksednbsdcfnfwtozioavvipvsrkztslcxqgrccocxtwnxobbhidcublbnpwhohqjcxwfftmptlwtpjugbchgxahplumbjqjfvljhqzmbdsdeemxevugsthrveucyqxdktkdymznwdvkuoytvfrrfzrmlnedhckhngadcpugwzfupcudmukkpzrtdqvpcpzspuhdfoeojybisjmcjmcyhiiqjnfkcpepbflwfwmorpgwumlzynzpbbvvrgtxpsgzdelmlohavhyqhrfztmncnllnfdgdotoiojwtwilwwdszhcqbkdwtyrurxkzgcwrcvqlhynujihfdbwnnhkwdmfwciurvrqkmyghvhftbfhjogfrrslmuzussufwkkiewfevkvgalhyutnfxzgxbifjhbqolbsanvwkhyfxywfbvxvoiwcqhvdypwpgquutrugldizlvqaeeboriznjxovvmbwqyrxmxqilplplszubphmeszzrfjoliuskludoukazpiezpzucrsiiiichlxthowlcbmmfnyjyylgrcseraqtwodnxvugpysbosancqgzmxinonoeqmvyumsdwjncgztbepamqupqvxzudrniawehxilhybtdsupswxzjfhhchdeqoidvigjhkonfrdskxvoskgezzhhcpcfodahrlnkoldcdomllfcywrtqofedeychinhsvcssmgbadabdgyvmscucbckahgjawopdwlixbkmlxcpxtaqoempcldkefcerzeiowhgyhreveztowuigsgwcvdjahrfvrvvubliwretdwqslwgusqoqcczbzdalaocaarmtqhgjtzjjwnntuezwioelmwxnvnfeeggjljuybgshzeqsongxutyjovbklauknymkkkmnnwqxixaiwaxfbysglyvazrrcqcbgepgegwlmtycljiaqivlscezkquxkgzubqnbdsfxditryyagiihyoqdhtudnfmkwaohttygtwesumjjivazppjzkbdywdfudbjkubytrfasxkxqmdgnirqronvypulppeaqbjimtvffglxvihsvesvhbagtuikytbocsjnxfoxmtwpfwcdadliexyisjopbkqbjhlflqyxnjdkqndjpbdehwfsljapruwbslzchkyvsmcvocictzqxcktfmoathqnxmlqirfjezhqbboupnzlyqmiqiqkkbhwhpcyibipmizzxhlbjffxdzigymhjgyowmrjouvfjwgyzdovyslmfbplvjnqvfdbfeqvugoqdzvtggrpueutlljsfgudmgrzjqiaghatyzwjbkxxadrwjohhqmnwrswodapavdwyvwicbignxagbqodjeihgvwbdlexjcrltkidjdzjjteihgwedogtxafmajjgfgprbtbktqvirgxvvakqhbvgizxdgmabszclfbkrchaubgcobhpqrtfjbjzhpllxyvuqinnnkzdwqxzjjbniytymygnjzmklhpvazfqcdhafvoxlkxnvsmzfhjcqwdzqmlblhduduwbpbwonfmfwwbvhbgoyhwlmlxfnhlfpzwiybgeqghufeqilmdxzcdwrdwiculhnhzxybxvkwpjbwyprvtphhhqsnukanpnzoxtumxwlgostwbgqmtvdzsecquyrircmlckkzviczrvtkzyazlihddrlohyrovhprvcsmjrbxjaivvgolidxbyvxgkflallznsylhuzrkhrvfakpbhwhrgtwnlczewkyxhcturbfbfvlwvhaykumdftqbkmdxutbnphdsgplxxsdkcfouaprhecugnzdsjdyjkkuvtjtberlrwxhddmshcoyzlrgwugpnozubiglbcjwxjnvnmnbdtvlfbqqijwmdkrzslhsvnxnrsdbkbyxfkluvtofyesakxclxvodsuxwlyqkoyhynxfmpvmecqxxasvmsdrandljnyeepxaiwdvmmrzxstnzzfkxjsflkkrabqkicjutpyrbaewqzwfwdhzjqibmqhhzbnoaucsbpjtvvumkpaehnxxsjgkfpbfannzznhylowtsnilprqrbohrmcucboxzqwnbkbkgldydkqqqgjbtxavejjlxfqweybeaczszapiqiqoqwzhrvnjlmjmdmyyziqcusbpyxqwetclyrhfjrgzxbydajuqnbxhmjgenskqjikmgqlpbmsvuuxehfbydyqvgdfnkdqhlptgaollttiduybwqgaaatmcvdhagbusjrjigyhcphyhowixnezvioigsjdosikthzijrdvsfabprlcmjtjekculxcoyvypsozolqezlgunkhsftyjrffpfkuxbuoolragvarmtjozwqfiqdlaldxdauwzdrlhxlghtovdwesahmzklfoywukjufdiyiepnyjqzqbvomvefaahlnbgjhvumffksfvomrbnfstssvdgpubtmglxicclsijqumvibauoaxvgteljaajfcrqadkxbqrgbwaihxdsaisopmmwbzddapbczwnfnxspgtajjswcubnspwxglemattdgijkavsoanafyrkczcvmxzciuvtiwnraibtfrdqcntksioxjlzstxivizavgurmvwphdfxcvwqicctqicommgehtlunpbknkkklbzcjrxcxjchbszlqhtcdkzbdktkffbbwufcvscjsaraktaatyexzjxvxvoyyzivxpmwuxxkjdkrrmfegzkevmaeotwvpcrjtbfsblfdebacvomgtudrlcrjktvwdaerlafaqfcopbqxujngvxmjelcuesauyxuazrhiztlapgvsdenyqpafckjzohjjbdosjyvombptrppmanummqvahchtqkjdppwwskbygzaqpjlxkiposgfwltwlkvowynkcytprknckyppzvjjqaqibhakstpgkpbhviuqdrnsazdfptdmheqeusmkskdldaqnxthokukmhcpssjrtjnemyvlsaeryoeiclipnrjmbiyzpzfprjeyhphuqtdgqsgmicalezpyoakygeorrhzuyzhqqddhrygeybtoanobkvbfgpchrbtqbampimgefkyrkdfqgwyulvqbzljzbrisjugfjpruwilxneypgflzfldsbkpymcmxfpedmwogtxqrifposbwmohakknpkdbdycsgetahejtlqjaoumqyjbxywbmpbtcgquedhtfbbptomabbnahguvzsayqgvqxolvuflfjfhvmilqdzwqusvlcgemlaouwlgluuqtrqlhwooretsjjtnpnvrpnicakqcfuxotzmvqhsvoptvqiletevbhfbrolhijwidauovqlnqwmwvfoxljrbjtbwuazkhpnxntigrbdlhwbtwtzlnginyooppgpilsuzzjvfhanrggtxcjfxmvgbfsipktduomcoukthptkxahkkivmbnikapysfahapdembxvuakdniziuslabaotlifsolqboplhuasrlawpjsjaheapmubdtysalursciiukkgtrkzmqaltyksvdmomgydqqswpkqmewzzyxifqiivisommszulngjdsovkgsahicjhnlxqutcsyhfhxxyamenvwbruzzkywgmcmnqzvkindlsworliooqshsbxvoctrjionbzsihjhfitybhqyajludzdmitakuritzrgpdkvqptsmrqojcagmrhjppgsovqgrgjzdpzmjcrjbqprzbuufhwjlfgjwokimhvihgkgnkuajkpfsbiragdwbggbjesipyihpinhcrhpobdiaasfdivbsjpqeobgbzszqdkoixnhihncdutlggytzukcbtrdvxgbdllkswarjqehcdddgqdvwxgjtyymecyvqsutnpnwygxvlxxrpggidpmoygidulrdnixkuuiwmigcsntnlvomivajdmmopbyqljbmkqueawblhaicmshjhwnxieiftzjwwrwameuuzcoqiuibpcsaajzdciyxsqaeubgixinvwlecbkrctrwtoskgbdjbyjlgvmydlqrymdhyfdqawurvxprrnfnymfuvenrfdwpnxfqsbylqfokjnmpvnrtoqnhzpgzsebieouetuuruwenrjbuwondepkkuvxfzyswbnlykxglazitalhyhtksszzhglorprfobxkihnwxghhybaaspqmucv", False),
    ("adc", "dcda", True)
]

if __name__ == "__main__":
    run_tests()
