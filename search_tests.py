from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    
    def test_keyword_to_titles(self):
        original_1 = ['French pop music', 'Mack Johnson', 1172208041, 5569, [ ]], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, []]
        expected_result_1 = {}
        self.assertEqual(keyword_to_titles(original_1), expected_result_1)

        original_2 = ['French pop music', 'Mack Johnson', 1172208041, 5569, ["dance"]], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ["dance"]]
        expected_result_2 = {"dance":['French pop music', 'Edogawa, Tokyo']}
        self.assertEqual(keyword_to_titles(original_2), expected_result_2)

        original_3 = ['French pop music', 'Mack Johnson', 1172208041, 5569, []], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ["dance"]]
        expected_result_3 = {"dance":['Edogawa, Tokyo']}
        self.assertEqual(keyword_to_titles(original_3), expected_result_3)

        original_4 = ['French pop music', 'Mack Johnson', 1172208041, 5569, []], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, [54]]
        expected_result_4 = {54:['Edogawa, Tokyo']}
        self.assertEqual(keyword_to_titles(original_4), expected_result_4)
    
        keyword_list_1 = [['French pop music', 'Mack Johnson', 1172208041, 5569, ['french', 'pop', 'music', 'the', 'france', 'and', 'radio']], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']], ['Noise (music)', 'jack johnson', 1194207604, 15641, ['1960', 'album', 'cassette', 'ubuweb', 'com', 'ubu']]]
        expected_keyword_to_titles_dict_1 = {'french': ['French pop music'], 'pop': ['French pop music'], 'music': ['French pop music'], 'the': ['French pop music', 'Edogawa, Tokyo'], 'france': ['French pop music'], 'and': ['French pop music', 'Edogawa, Tokyo'], 'radio': ['French pop music'], 'edogawa': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo'], '1960': ['Noise (music)'], 'album': ['Noise (music)'], 'cassette': ['Noise (music)'], 'ubuweb': ['Noise (music)'], 'com': ['Noise (music)'], 'ubu': ['Noise (music)']}
        self.assertEqual(keyword_to_titles(keyword_list_1), expected_keyword_to_titles_dict_1)


        keyword_list_2 = []
        expected_keyword_to_titles_dict_2 = {}
        self.assertEqual(keyword_to_titles(keyword_list_2), expected_keyword_to_titles_dict_2)


        keyword_list_3 = ''
        expected_keyword_to_titles_dict_3 = {}
        self.assertEqual(keyword_to_titles(keyword_list_3), expected_keyword_to_titles_dict_3)



    def test_title_to_info(self):
        original_1 = ['French pop music', 'Mack Johnson', 1172208041, 5569, [ ]], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ["dance"]]
        expected_result_1 = {'French pop music':{'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}
        self.assertEqual(title_to_info(original_1), expected_result_1)

        original_2 = ['French pop music', 'Mack Johnson', 1172208041, 5569, ["dance"]], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ["dance","music",18999]]
        expected_result_2 = {'French pop music':{'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}
        self.assertEqual(title_to_info(original_2), expected_result_2)

        original_3 = ['French pop music', 'Mack Johnson', 1172208041, 5569, []], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, []]
        expected_result_3 = {'French pop music':{'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}
        self.assertEqual(title_to_info(original_3), expected_result_3)

        whole_data = article_metadata()
        expected_result = {'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'French pop music': {'author': 'Mack Johnson', 'timestamp': 1172208041, 'length': 5569}, 'Edogawa, Tokyo': {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}, 'Noise (music)': {'author': 'jack johnson', 'timestamp': 1194207604, 'length': 15641}, '1922 in music': {'author': 'Gary King', 'timestamp': 1242717698, 'length': 11576}, 'Ken Kennedy (computer scientist)': {'author': 'Mack Johnson', 'timestamp': 1246308670, 'length': 4144}, '1986 in music': {'author': 'jack johnson', 'timestamp': 1048918054, 'length': 6632}, 'Spain national beach soccer team': {'author': 'jack johnson', 'timestamp': 1233458894, 'length': 1526}, 'Kevin Cadogan': {'author': 'Mr Jake', 'timestamp': 1144136316, 'length': 3917}, 'Endogenous cannabinoid': {'author': 'Pegship', 'timestamp': 1168971903, 'length': 26}, '2009 in music': {'author': 'RussBot', 'timestamp': 1235133583, 'length': 69451}, 'Rock music': {'author': 'Mack Johnson', 'timestamp': 1258069053, 'length': 119498}, 'Medical value travel': {'author': 'jack johnson', 'timestamp': 1153157342, 'length': 4149}, 'Lights (musician)': {'author': 'Burna Boy', 'timestamp': 1213914297, 'length': 5898}, 'List of soul musicians': {'author': 'jack johnson', 'timestamp': 1175455921, 'length': 4878}, 'Human computer': {'author': 'Bearcat', 'timestamp': 1248275178, 'length': 4750}, 'Aube (musician)': {'author': 'Mack Johnson', 'timestamp': 1145410600, 'length': 3152}, 'List of overtone musicians': {'author': 'Mack Johnson', 'timestamp': 1176928050, 'length': 2299}, 'Black dog (ghost)': {'author': 'Pegship', 'timestamp': 1220471117, 'length': 14746}, 'USC Trojans volleyball': {'author': 'jack johnson', 'timestamp': 1218049435, 'length': 5525}, 'Tim Arnold (musician)': {'author': 'jack johnson', 'timestamp': 1181480380, 'length': 4551}, '2007 Bulldogs RLFC season': {'author': 'Burna Boy', 'timestamp': 1177410119, 'length': 11116}, 'Peter Brown (music industry)': {'author': 'Pegship', 'timestamp': 1240235639, 'length': 2837}, 'Mexican dog-faced bat': {'author': 'Mack Johnson', 'timestamp': 1255316429, 'length': 1138}, 'Embryo drawing': {'author': 'Jack Johnson', 'timestamp': 1034459202, 'length': 1712}, 'Old-time music': {'author': 'Nihonjoe', 'timestamp': 1124771619, 'length': 12755}, 'Arabic music': {'author': 'RussBot', 'timestamp': 1209417864, 'length': 25114}, 'C Sharp (programming language)': {'author': 'Burna Boy', 'timestamp': 1232492672, 'length': 52364}, 'List of Saturday Night Live musical sketches': {'author': 'Pegship', 'timestamp': 1134966249, 'length': 13287}, 'Joe Becker (musician)': {'author': 'Nihonjoe', 'timestamp': 1203234507, 'length': 5842}, 'Will Johnson (soccer)': {'author': 'Burna Boy', 'timestamp': 1218489712, 'length': 3562}, 'Aco (musician)': {'author': 'Nihonjoe', 'timestamp': 1132546632, 'length': 3129}, 'Geoff Smith (British musician)': {'author': 'Pegship', 'timestamp': 1194687509, 'length': 2043}, 'Fiskerton, Lincolnshire': {'author': 'Bearcat', 'timestamp': 1259869948, 'length': 5853}, 'Reflection-oriented programming': {'author': 'Nihonjoe', 'timestamp': 1143366937, 'length': 38}, 'B (programming language)': {'author': 'jack johnson', 'timestamp': 1196622610, 'length': 5482}, 'Richard Wright (musician)': {'author': 'RussBot', 'timestamp': 1189536295, 'length': 16185}, 'Voice classification in non-classical music': {'author': 'RussBot', 'timestamp': 1198092852, 'length': 11280}, 'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}, '1936 in music': {'author': 'RussBot', 'timestamp': 1243745950, 'length': 23417}, 'Guide dog': {'author': 'Jack Johnson', 'timestamp': 1165601603, 'length': 7339}, '1962 in country music': {'author': 'Mack Johnson', 'timestamp': 1249862464, 'length': 7954}, 'List of dystopian music, TV programs, and games': {'author': 'Bearcat', 'timestamp': 1165317338, 'length': 13458}, 'Steven Cohen (soccer)': {'author': 'Mack Johnson', 'timestamp': 1237669593, 'length': 2117}, 'Steve Perry (musician)': {'author': 'Nihonjoe', 'timestamp': 1254812045, 'length': 22204}, '2009 Louisiana Tech Bulldogs football team': {'author': 'Nihonjoe', 'timestamp': 1245796406, 'length': 22410}, 'David Gray (musician)': {'author': 'jack johnson', 'timestamp': 1159841492, 'length': 7203}, 'Craig Martin (soccer)': {'author': 'Mr Jake', 'timestamp': 1174203493, 'length': 709}, 'Georgia Bulldogs football': {'author': 'Burna Boy', 'timestamp': 1166567889, 'length': 43718}, 'Time travel': {'author': 'Jack Johnson', 'timestamp': 1140826049, 'length': 35170}, 'Fisk University': {'author': 'RussBot', 'timestamp': 1263393671, 'length': 16246}, 'Annie (musical)': {'author': 'Jack Johnson', 'timestamp': 1223619626, 'length': 27558}, 'Alex Turner (musician)': {'author': 'jack johnson', 'timestamp': 1187010135, 'length': 9718}, 'Python (programming language)': {'author': 'Burna Boy', 'timestamp': 1137530195, 'length': 41571}, 'List of gospel musicians': {'author': 'Nihonjoe', 'timestamp': 1197658845, 'length': 3805}, 'Tom Hooper (musician)': {'author': 'Bearcat', 'timestamp': 1204967541, 'length': 1441}, 'Endoglin': {'author': 'Bearcat', 'timestamp': 1212259031, 'length': 6778}, 'Indian classical music': {'author': 'Burna Boy', 'timestamp': 1222543238, 'length': 9503}, 'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}, '1996 in music': {'author': 'Nihonjoe', 'timestamp': 1148585201, 'length': 21688}, 'Lua (programming language)': {'author': 'Burna Boy', 'timestamp': 1113957128, 'length': 0}, 'Single-board computer': {'author': 'Gary King', 'timestamp': 1220260601, 'length': 8271}, 'Mets de Guaynabo (volleyball)': {'author': 'Mr Jake', 'timestamp': 1239156764, 'length': 2091}, "United States men's national soccer team 2009 results": {'author': 'Burna Boy', 'timestamp': 1252384026, 'length': 79089}, 'Joseph Williams (musician)': {'author': 'Pegship', 'timestamp': 1140752684, 'length': 4253}, 'The Hunchback of Notre Dame (musical)': {'author': 'Nihonjoe', 'timestamp': 1192176615, 'length': 42}, 'China national soccer team': {'author': 'RussBot', 'timestamp': 1199103839, 'length': 45}, 'Covariance and contravariance (computer science)': {'author': 'Bearcat', 'timestamp': 1167547364, 'length': 7453}, 'English folk music (1500–1899)': {'author': 'Bearcat', 'timestamp': 1177634764, 'length': 2073}, 'Personal computer': {'author': 'Pegship', 'timestamp': 1220391790, 'length': 45663}, 'The Mandogs': {'author': 'Mack Johnson', 'timestamp': 1205282029, 'length': 3968}, 'David Levi (musician)': {'author': 'Gary King', 'timestamp': 1212260237, 'length': 3949}, 'Scores (computer virus)': {'author': 'RussBot', 'timestamp': 1235850703, 'length': 2706}, 'Digital photography': {'author': 'Mr Jake', 'timestamp': 1095727840, 'length': 18093}, 'George Crum (musician)': {'author': 'jack johnson', 'timestamp': 1252996687, 'length': 3848}, 'Solver (computer science)': {'author': 'Gary King', 'timestamp': 1253282654, 'length': 1861}, 'Georgia Bulldogs football under Robert Winston': {'author': 'jack johnson', 'timestamp': 1166046122, 'length': 1989}, 'Wildlife photography': {'author': 'Jack Johnson', 'timestamp': 1165248747, 'length': 1410}, 'Traditional Thai musical instruments': {'author': 'Jack Johnson', 'timestamp': 1191830919, 'length': 6775}, 'Landseer (dog)': {'author': 'Bearcat', 'timestamp': 1231438650, 'length': 2006}, 'Charles McPherson (musician)': {'author': 'Bearcat', 'timestamp': 1255183865, 'length': 3007}, 'Comparison of programming languages (basic instructions)': {'author': 'RussBot', 'timestamp': 1238781354, 'length': 61644}, 'Les Cousins (music club)': {'author': 'Mack Johnson', 'timestamp': 1187072433, 'length': 4926}, 'Paul Carr (musician)': {'author': 'Burna Boy', 'timestamp': 1254142018, 'length': 5716}, '2006 in music': {'author': 'Jack Johnson', 'timestamp': 1171547747, 'length': 105280}, 'Spawning (computer gaming)': {'author': 'jack johnson', 'timestamp': 1176750529, 'length': 3413}, 'Sean Delaney (musician)': {'author': 'Nihonjoe', 'timestamp': 1204328174, 'length': 5638}, 'Tony Kaye (musician)': {'author': 'Burna Boy', 'timestamp': 1141489894, 'length': 8419}, 'Danja (musician)': {'author': 'RussBot', 'timestamp': 1257155543, 'length': 6925}, 'Ruby (programming language)': {'author': 'Bearcat', 'timestamp': 1193928035, 'length': 30284}, 'Texture (music)': {'author': 'Bearcat', 'timestamp': 1161070178, 'length': 3626}, 'List of computer role-playing games': {'author': 'Mr Jake', 'timestamp': 1179441080, 'length': 43088}, 'Register (music)': {'author': 'Pegship', 'timestamp': 1082665179, 'length': 598}, 'Mode (computer interface)': {'author': 'Pegship', 'timestamp': 1182732608, 'length': 2991}, '2007 in music': {'author': 'Bearcat', 'timestamp': 1169248845, 'length': 45652}, 'List of video games with time travel': {'author': 'Mack Johnson', 'timestamp': 1234110556, 'length': 2344}, '2008 in music': {'author': 'Burna Boy', 'timestamp': 1217641857, 'length': 107605}, 'Semaphore (programming)': {'author': 'Nihonjoe', 'timestamp': 1144850850, 'length': 7616}, "Wake Forest Demon Deacons men's soccer": {'author': 'Burna Boy', 'timestamp': 1260577388, 'length': 26745}}
        self.assertEqual(title_to_info(whole_data), expected_result)


    def test_search(self):
        expected_result_1 = ['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog']
        self.assertEqual(search('dog', keyword_to_titles(article_metadata())),expected_result_1)

        expected_result_2 = []
        self.assertEqual(search('DOG', keyword_to_titles(article_metadata())),expected_result_2)

        expected_result_3 = []
        self.assertEqual(search('DO', keyword_to_titles(article_metadata())),expected_result_3)

        expected_result_4 = []
        self.assertEqual(search('', keyword_to_titles(article_metadata())),expected_result_4)


    def test_article_length(self):
        expected_result_1 = ['List of Canadian musicians', 'Lights (musician)', 'Old-time music', 'Will Johnson (soccer)'] 
        self.assertEqual(article_length(500000,search('canada', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), expected_result_1)

        expected_result_2 = [] 
        self.assertEqual(article_length(50,search('canada', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), expected_result_2)

        expected_result_3 = [] 
        self.assertEqual(article_length(50000000,search('Canada', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), expected_result_3)

        expected_result_4 = [] 
        self.assertEqual(article_length(-8,search('canada', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), expected_result_4)

        expected_result_5 = [] 
        self.assertEqual(article_length(5000000,search('', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), expected_result_5)




    def test_key_by_author(self):
        expected_result_1 = {'Jack Johnson': ['List of Canadian musicians'], 'Burna Boy': ['Lights (musician)', 'Will Johnson (soccer)'], 'Nihonjoe': ['Old-time music']}
        self.assertEqual(key_by_author(search('canada', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), expected_result_1)

        expected_result_2 = {}
        self.assertEqual(key_by_author(search('Canada', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), expected_result_2)

        expected_result_3 = {}
        self.assertEqual(key_by_author(search('', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), expected_result_3)

    
    
    def test_filter_out(self):
        expected_result_1 = ['Lights (musician)', 'Old-time music', 'Will Johnson (soccer)']
        self.assertEqual(filter_out("artist", search('canada', keyword_to_titles(article_metadata())), keyword_to_titles(article_metadata())), expected_result_1)











    




    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_1(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_2(self, input_mock):
        keyword = 'canada'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'Jack Johnson': ['List of Canadian musicians'], 'Burna Boy': ['Lights (musician)', 'Will Johnson (soccer)'], 'Nihonjoe': ['Old-time music']}\n"
        
        self.assertEqual(output,expected)
    
    @patch('builtins.input')
    def test_3(self, input_mock):
        keyword = 'dog'
        advanced_option = 3
        advanced_response = "Mr Jake"

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Dalmatian (dog)', 'Sun dog']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_4(self, input_mock):
        keyword = 'soccer'
        advanced_option = 4
        advanced_response = "ball"

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_6(self, input_mock):
        keyword = 'canada'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['List of Canadian musicians', 'Lights (musician)', 'Old-time music', 'Will Johnson (soccer)']\n"

        self.assertEqual(output,expected)


 

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()