##### NLTK CHAPTER 1 NOTES & EXERCISES #####

# Below is from preface, used to print any words that end in "ing" from the given text file
# I chose random characters and words for tester.txt
for line in open("tester.txt"):
	for word in line.split():
		if word.endswith('ing'):
			print(word)
 
### NOTES (from nltk.book import *) ###
sometext.concordance("some word/phrase"): shows all instances of the word in the text

sometext.similar("some word/phrase"): lists the words that appear in similar contexts
		ie. sometext.similar("happy") in the contexts of "a happy girl" or "the happy occasion" 
			will turn up words like "sad" if used in the same contexts if they are in the text 
			("a sad girl", "the sad occasion")

sometext.common_contexts(["some word", "some other word", "nth word"]): shows all the shared contexts 
	of the listed words
		ie. sometext.common_contexts(["happy", "sad"]) -> a_girl, the_occasion

sometext.dispersion_plot(["some word", "some other word", "nth word"]): displays a dispersion plot 
	of the listed words based on the offset number of words from the beginning; allows us to see 
	how far into the text the word(s) appear

sometext.generate(): generates some random text in the style of sometext

FreqDist(sometext): creates a frequency distribution of all distinct tokens in the text

somefreqdist.most_common(some number n): lists the n most common tokens and their counts in the 
	frequency distribution, from most to least frequent

somefreqdist[some token]: retrieves the frequency associated with the token in the frequency distribution
	(kind of like a dictionary key)

bigrams(list of tokens): generator function for the list of tokens, which yields the tokens in pairs
	with the token one index greater
		ie. list(bigrams(["hello", "hi", "world", "there"])) returns [('hello', 'hi'), ('hi', 'world'), ('world', 'there')]

sometext.collocations(): shows all the collocations in the text (pretty much just frequent bigrams)

# set(some text or list of tokens) function basically returns a set of all distinct tokens/words 
#	(word types) from the input

# some text or list of tokens with .count(some word) returns the count of that word in the text/tokens 

# lexical diversity: percentage of distinct words in a text

# collocation: a set of words that occur together unusually often (ie. "red wine" but not "the wine"); 
#	typically resistant to substitution with words that have similar senses
#		ie. "maroon wine" doesn't really make sense

# string1.join(list of strings): inserts string1 between each element of the list


### EXERCISES ###

# note: skipped some exercises because they are based on playing around in the interpreter 

2. 26 ** 100
3. ['Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 
	'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 
	'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 
	'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python']
4. 141576 words in text2; 6833 distinct words
5. humor has more lexical diversity
6. Elinor seems to be the main character, closely followed by Marianne; Elinor & Edward, Marianne & Willoughby
	are probably the couples
7. text5 collocations below, commented out due to formatting issues
	# 	wanna chat; PART JOIN; MODE #14-19teens; JOIN PART; PART PART;
	# 	cute.-ass MP3; MP3 player; JOIN JOIN; times .. .; ACTION watches; guys
	# 	wanna; song lasts; last night; ACTION sits; -...)...- S.M.R.; Lime
	# 	Player; Player 12%; dont know; lez gurls; long time
8. returns a list of distinct tokens in text4, then finds the length of that list
9. could fix spacing issues with " ".join(the resulting list)
11. same length
12. probably the first one; it is more precise
13. substring of a word at the double index
14. 5, 8
15. ['b', 'b-day', 'b/c', 'b4', 'babay', 'babble', 'babblein', 'babe', 'babes', 'babi', 'babies', 'babiess', 
	'baby', 'babycakeses', 'bachelorette', 'back', 'backatchya', 'backfrontsidewaysandallaroundtheworld', 'backroom', 
	'backup', 'bacl', 'bad', 'bag', 'bagel', 'bagels', 'bahahahaa', 'bak', 'baked', 'balad', 'balance', 'balck', 'ball', 
	'ballin', 'balls', 'ban', 'band', 'bandito', 'bandsaw', 'banjoes', 'banned', 'baord', 'bar', 'barbie', 'bare', 
	'barely', 'bares', 'barfights', 'barks', 'barn', 'barrel', 'base', 'bases', 'basically', 'basket', 'battery', 'bay', 
	'bbbbbyyyyyyyeeeeeeeee', 'bbiam', 'bbl', 'bbs', 'bc', 'be', 'beach', 'beachhhh', 'beam', 'beams', 'beanbag', 'beans', 
	'bear', 'bears', 'beat', 'beaten', 'beatles', 'beats', 'beattles', 'beautiful', 'because', 'beckley', 'become', 'bed', 
	'bedford', 'bedroom', 'beeeeehave', 'beeehave', 'been', 'beer', 'before', 'beg', 'begin', 'behave', 'behind', 'bein', 
	'being', 'beleive', 'believe', 'belive', 'bell', 'belly', 'belong', 'belongings', 'ben', 'bend', 'benz', 'bes', 
	'beside', 'besides', 'best', 'bet', 'betrayal', 'betta', 'better', 'between', 'beuty', 'bf', 'bi', 'biatch', 'bible', 
	'biebsa', 'bied', 'big', 'bigest', 'biggest', 'biiiatch', 'bike', 'bikes', 'bikini', 'bio', 'bird', 'birfday', 
	'birthday', 'bisexual', 'bishes', 'bit', 'bitch', 'bitches', 'bitdh', 'bite', 'bites', 'biyatch', 'biz', 'bj', 
	'black', 'blade', 'blah', 'blank', 'blankie', 'blazed', 'bleach', 'blech', 'bless', 'blessings', 'blew', 'blind', 
	'blinks', 'bliss', 'blocking', 'bloe', 'blood', 'blooded', 'bloody', 'blow', 'blowing', 'blowjob', 'blowup', 'blue', 
	'blueberry', 'bluer', 'blues', 'blunt', 'board', 'bob', 'bodies', 'body', 'boed', 'boght', 'boi', 'boing', 'boinked', 
	'bois', 'bomb', 'bone', 'boned', 'bones', 'bong', 'boning', 'bonus', 'boo', 'booboo', 'boobs', 'book', 'boom', 
	'boooooooooooglyyyyyy', 'boost', 'boot', 'bootay', 'booted', 'boots', 'booty', 'border', 'borderline', 'bored', 
	'boredom', 'boring', 'born', 'born-again', 'bosom', 'boss', 'bossy', 'bot', 'both', 'bother', 'bothering', 'bottle', 
	'bought', 'bounced', 'bouncer', 'bouncers', 'bound', 'bout', 'bouts', 'bow', 'bowl', 'box', 'boy', 'boyfriend', 'boys', 
	'bra', 'brad', 'brady', 'brain', 'brakes', 'brass', 'brat', 'brb', 'brbbb', 'bread', 'break', 'breaks', 'breath', 
	'breathe', 'bred', 'breeding', 'bright', 'brightened', 'bring', 'brings', 'bro', 'broke', 'brooklyn', 'brother', 
	'brothers', 'brought', 'brown', 'brrrrrrr', 'bruises', 'brunswick', 'brwn', 'btw', 'bucks', 'buddyyyyyy', 'buff', 
	'buffalo', 'bug', 'bugs', 'buh', 'build', 'builds', 'built', 'bull', 'bulls', 'bum', 'bumber', 'bummer', 'bumped', 
	'bumper', 'bunch', 'bunny', 'burger', 'burito', 'burned', 'burns', 'burp', 'burpin', 'burps', 'burried', 'burryed', 
	'bus', 'buses', 'bust', 'busted', 'busy', 'but', 'butt', 'butter', 'butterscotch', 'button', 'buttons', 'buy', 'buying', 
	'bwahahahahahahahahahaha', 'by', 'byb', 'bye', 'byeee', 'byeeee', 'byeeeeeeee', 'byeeeeeeeeeeeee', 'byes']
17. 621:644
18. ['!', ',', '-', '.', '1', '25', '29', '61', ':', 'ARTHUR', 'Call', 'Citizens', 'Dashwood', 'Fellow', 'God', 'House', 
	'I', 'In', 'Ishmael', 'JOIN', 'KING', 'MALE', 'Nov.', 'PMing', 'Pierre', 'Representatives', 'SCENE', 'SEXY', 'Senate', 
	'Sussex', 'The', 'Vinken', 'Whoa', '[', ']', 'a', 'and', 'as', 'attrac', 'been', 'beginning', 'board', 'clop', 'created', 
	'director', 'discreet', 'earth', 'encounters', 'family', 'for', 'had', 'have', 'heaven', 'in', 'join', 'lady', 'lol', 
	'long', 'me', 'nonexecutive', 'of', 'old', 'older', 'people', 'problem', 'seeks', 'settled', 'single', 'the', 'there', 
	'to', 'will', 'wind', 'with', 'years']
19. line 1 lowercases every word in text1, then sorts the set of distinct words that results. line 2 lowercases every 
	word in the set of distinct words in text1, then sorts the resulting words.  The key difference is that line 1 would
	consider "Hello" and "hello" to be ultimately the same, whereas line 2 considers their initial forms to be different,
	despite the fact that they both ultimately end up "hello"
20. someword.isupper() checks if someword contains cased characters and all are uppercase; someword.islower() checks 
	if someword contains cased characters and all are lowercase.  They are not mutually exclusive in being true or false, 
	because someword could contain a non-cased character (ie. a number in a string like "1"), and both functions would
	return false
21. text2[-2:]
22. [('JOIN', 1021), ('PART', 1016), ('that', 274), ('what', 183), ('here', 181), ('....', 170), ('have', 164), ('like', 156), 
	('with', 152), ('chat', 142), ('your', 137), ('good', 130), ('just', 125), ('lmao', 107), ('know', 103), ('room', 98), 
	('from', 92), ('this', 86), ('well', 81), ('back', 78), ('hiya', 78), ('they', 77), ('dont', 75), ('yeah', 75), ('want', 71), 
	('love', 60), ('guys', 58), ('some', 58), ('been', 57), ('talk', 56), ('nice', 52), ('time', 50), ('when', 48), ('haha', 44), 
	('make', 44), ('girl', 43), ('need', 43), ('U122', 42), ('MODE', 41), ('will', 40), ('much', 40), ('then', 40), ('over', 39), 
	('work', 38), ('were', 38), ('take', 37), ('U121', 36), ('U115', 36), ('song', 36), ('even', 35), ('does', 35), ('seen', 35), 
	('U156', 35), ('U105', 35), ('more', 34), ('damn', 34), ('only', 33), ('come', 33), ('hell', 29), ('long', 28), ('them', 28), 
	('name', 27), ('tell', 27), ('away', 26), ('sure', 26), ('look', 26), ('baby', 26), ('call', 26), ('play', 25), ('U110', 25), 
	('U114', 25), ('NICK', 24), ('down', 24), ('cool', 24), ('sexy', 23), ('many', 23), ('hate', 23), ('said', 23), ('last', 22), 
	('ever', 22), ('hear', 21), ('life', 21), ('live', 20), ('feel', 19), ('very', 19), ('mean', 19), ('give', 19), ('same', 19), 
	('must', 19), ('stop', 19), ('LMAO', 19), ('!!!!', 18), ('hugs', 18), ('What', 18), ('find', 18), ('cant', 18), ('left', 17), 
	('????', 17), ('shit', 17), ('nite', 17), ('busy', 17), ('hair', 17), ('lost', 17), ('U104', 17), ('fine', 16), ('real', 16), 
	('game', 16), ('fuck', 15), ('sits', 15), ('eyes', 15), ('lets', 15), ('heya', 15), ('kill', 15), ('read', 14), ('shut', 14), 
	('wait', 14), ('goes', 14), ('keep', 14), ('true', 14), ('pick', 13), ('free', 13), ('else', 13), ('near', 13), ('nope', 13), 
	('U168', 13), ('hope', 12), ('head', 12), ('male', 12), ('than', 12), ('gets', 12), ('cold', 12), ('hehe', 12), ('bout', 12), 
	('stay', 12), ('used', 12), ('awww', 12), ('told', 12), ('This', 12), ('U102', 12), ('doin', 11), ('kids', 11), ('perv', 11), 
	('wont', 11), ('face', 11), ('home', 11), ('year', 11), ('babe', 11), ('into', 11), ('yall', 11), ('.. .', 11), ('U119', 11), 
	('U107', 11), ('hard', 10), ('show', 10), ('U101', 10), ('once', 10), ('Well', 10), ('help', 10), ('mind', 10), ('Yeah', 10), 
	('week', 10), ('Liam', 10), ('U132', 10), ('pics', 9), ('such', 9), ('type', 9), ('best', 9), ('neck', 9), ('dang', 9), 
	('dead', 9), ('runs', 9), ('aint', 9), ('rock', 9), ('days', 9), ('mine', 9), ('book', 9), ('crap', 9), ('soon', 9), 
	('care', 9), ('full', 9), ('kiss', 9), ('hour', 9), ('nick', 9), ('sick', 9), ('; ..', 9), ('hmmm', 9), ('U139', 8), 
	('word', 8), ('heyy', 8), ('case', 8), ('wana', 8), ('hows', 8), ('went', 8), ('lady', 8), ('blue', 8), ('says', 8), 
	('suck', 8), ('made', 8), ('wife', 8), ('sang', 8), ('U144', 8), ('fast', 7), ('rule', 7), ('dude', 7), ('okay', 7), 
	('alot', 7), ('hand', 7), ('took', 7), ('wear', 7), ('Hiya', 7), ('kick', 7), ('ahhh', 7), ('dear', 7), ('That', 7), 
	('U108', 7), ('U169', 7), ('U129', 6), ('U116', 6), ('most', 6), ('thru', 6), ('U165', 6), ('list', 6), ('seem', 6), 
	('sing', 6), ('next', 6), ('done', 6), ('ride', 6), ('comp', 6), ('main', 6), ('))))', 6), ('goin', 6), ('U520', 6), 
	('pink', 6), ('poor', 6), ('gone', 6), ('oops', 6), ('knew', 6), ('<---', 6), ('ball', 6), ('send', 6), ('Song', 6), 
	('blah', 6), ('They', 6), ('part', 6), ('U103', 6), ('U120', 6), ('Last', 6), ('whos', 6), ('food', 6), ('U142', 6), 
	('sock', 6), ('U197', 6), ('legs', 5), ('fire', 5), ('warm', 5), ('late', 5), ('hang', 5), ('miss', 5), ('boys', 5), 
	('land', 5), ('nose', 5), ('lick', 5), ('caps', 5), ('wish', 5), ('U128', 5), ('came', 5), ('cali', 5), ('roll', 5), 
	('easy', 5), ('lose', 5), ('When', 5), ('soul', 5), ('luck', 5), ('also', 5), ('kool', 5), ('fall', 5), ('boss', 5), 
	('beer', 5), ('ohhh', 5), ('####', 5), ('wall', 5), ('Have', 5), ('meet', 5), ('till', 5), ('feet', 5), ('xbox', 5), 
	('idea', 5), ('heck', 5), ('joke', 5), ('fool', 5), ('felt', 5), ('yoko', 5), ('meds', 5), ('both', 5), ('Lime', 5), 
	('glad', 4), ('U133', 4), ('U126', 4), ('jerk', 4), ('ugly', 4), ('date', 4), ('ummm', 4), ('quit', 4), ('rest', 4), 
	('door', 4), ('none', 4), ('self', 4), ('pass', 4), ('line', 4), ('cute', 4), ('holy', 4), ('hook', 4), ('Like', 4), 
	('each', 4), ('open', 4), ('high', 4), ('ouch', 4), ('evil', 4), ('fart', 4), ('grrr', 4), ('pain', 4), ('pfft', 4), 
	('sigh', 4), ('shes', 4), ('ROOM', 4), (',,,,', 4), ('lord', 4), ('mmmm', 4), ('ones', 4), ('huge', 4), ('woot', 4), 
	('shot', 4), ('team', 4), ('ways', 4), ('beat', 4), ('kent', 4), ('U130', 4), ('U196', 4), ('U219', 4), ('turn', 4), 
	('lame', 4), ('U123', 4), ('U154', 4), ('U988', 4), ('puff', 4), ('U146', 4), ('U989', 4), ('U117', 4), ('U819', 4), 
	('U820', 4), ('clap', 3), ('itch', 3), ('guyz', 3), ('U136', 3), ('gold', 3), ('ring', 3), ('isnt', 3), ('U141', 3), 
	('Only', 3), ('U148', 3), ('Your', 3), ('deal', 3), ('wash', 3), ('U109', 3), ('piff', 3), ('jump', 3), ('band', 3), 
	('orgy', 3), ('slap', 3), ('soft', 3), ('bend', 3), ('toss', 3), ('amen', 3), ('rain', 3), ('deop', 3), ('roof', 3), 
	('((((', 3), ('CHAT', 3), ('ahem', 3), ('hola', 3), ('butt', 3), ('imma', 3), ('town', 3), ('hawt', 3), ('2006', 3), 
	('Elev', 3), ('Wind', 3), ('AKDT', 3), ('lead', 3), ('DING', 3), ('note', 3), ('gawd', 3), ('half', 3), ('mary', 3), 
	('ello', 3), ('hick', 3), ('wine', 3), ('hiii', 3), ('bare', 3), ('vote', 3), ('Same', 3), ('wack', 3), ('snow', 3), 
	('hurt', 3), ('move', 3), ('road', 3), ('walk', 3), ('yawn', 3), ('hail', 3), ('nana', 3), ('U106', 3), ('hump', 3), 
	('elle', 3), ('yada', 3), ('tune', 3), ('hank', 3), ('slow', 3), ('rubs', 3), ('skin', 3), ('died', 3), ('U145', 3), 
	('swim', 3), ('U163', 3), ('army', 3), ('THAT', 3), ('wazz', 3), ('toes', 3), ('U153', 3), ('golf', 2), ('drew', 2), 
	('cast', 2), ('Days', 2), ('opps', 2), ('U138', 2), ('plan', 2), ('Just', 2), ('deaf', 2), ('deep', 2), ('phil', 2), 
	('hmph', 2), ('U155', 2), ('Poor', 2), ('Lies', 2), ('bite', 2), ('mins', 2), ('eats', 2), ('>:->', 2), ('cell', 2), 
	('cmon', 2), ('wats', 2), ('kind', 2), ('mike', 2), ('whoa', 2), ('dumb', 2), ('park', 2), ('Sure', 2), ('Come', 2), 
	('O.k.', 2), ('mama', 2), ('Nice', 2), ('hold', 2), ('ohio', 2), ('whip', 2), ('twin', 2), ('burp', 2), ('blew', 2), 
	('temp', 2), ('corn', 2), ('pool', 2), ('cash', 2), ('ears', 2), ('From', 2), ('porn', 2), ('heal', 2), ('Dang', 2), 
	('ciao', 2), ('DOES', 2), ('typo', 2), ('Stop', 2), ('eric', 2), ('Drew', 2), ('sore', 2), ('Live', 2), ('High', 2), 
	('hits', 2), ('KoOL', 2), ('past', 2), ('Love', 2), ('meat', 2), ('!!!.', 2), ('argh', 2), ('limp', 2), ('rent', 2), 
	('cars', 2), ('Tell', 2), ('shop', 2), ('U172', 2), ('five', 2), ('sell', 2), ('<<<<', 2), ('city', 2), ('yard', 2), 
	('grrl', 2), ('chip', 2), ('bear', 2), ('foot', 2), ('uses', 2), ('DONT', 2), ('sort', 2), ('lies', 2), ('whud', 2), 
	('hott', 2), ('Down', 2), ('Lets', 2), ('club', 2), ('adds', 2), ('Here', 2), ('born', 2), ('wOOt', 2), ('area', 2), 
	('?!?!', 2), ('Ohio', 2), ('U112', 2), ('humm', 2), ('newp', 2), ('gays', 2), ('zone', 2), ('hint', 2), ('spin', 2), 
	('ewww', 2), ('pies', 2), ('doll', 2), ('drop', 2), ('gimp', 2), ('spot', 2), ('ages', 2), ('clue', 2), ('mass', 2), 
	('Ummm', 2), ('Gosh', 2), ('flow', 2), ('kewl', 2), ('hall', 2), ('haze', 2), ('1996', 2), ('John', 2), ('john', 2), 
	('sooo', 2), ('cost', 2), ('trip', 2), ('babi', 2), ('rich', 2), ('U100', 2), ('n9ne', 2), ('Ahhh', 2), ('??!!', 2), 
	('U111', 2), ('moon', 2), ('STOP', 2), ('any1', 2), ('yeas', 2), ('wooo', 2), ('<333', 2), ('tick', 2), ('tock', 2), 
	('WITH', 2), ('FROM', 2), ('side', 2), ('Heyy', 2), ('howz', 2), ("ex's", 2), ('Cool', 2), ('U170', 2), ('U175', 2), 
	('root', 2), ('tyvm', 2), ('luvs', 2), ('fits', 2), ('rofl', 2), ('sand', 2), ('ltns', 2), ('flaw', 2), ('aunt', 2), 
	('lawl', 2), ('Okay', 2), ('HAVE', 2), ('NONE', 2), ('YOUR', 2), ('Lmao', 2), ('Tisk', 2), ('U190', 2), ('tisk', 2), 
	('draw', 1), ('docs', 1), ('Slip', 1), ('Fade', 1), ('bowl', 1), ('bong', 1), ('ogan', 1), ('cams', 1), ('gooo', 1), 
	('yeee', 1), ('ahah', 1), ('jeep', 1), ('Deep', 1), ('Show', 1), ('Turn', 1), ('Hand', 1), ('VBox', 1), ('ELSE', 1), 
	('serg', 1), ('bein', 1), ('whys', 1), ('tape', 1), ('sexs', 1), ('form', 1), ('HUGE', 1), ('nads', 1), ('owww', 1), 
	('gags', 1), ('Meep', 1), ('LAst', 1), ("pm's", 1), ('1.99', 1), ('lool', 1), ('kina', 1), ('sext', 1), ('lazy', 1), 
	('calm', 1), ('arms', 1), ('smax', 1), ('VVil', 1), ('este', 1), ('chik', 1), ('Boyz', 1), ('coat', 1), ('Eyes', 1), 
	('Dawn', 1), ('LIVE', 1), ('mauh', 1), ('ques', 1), ('4.20', 1), ('gosh', 1), ('ruff', 1), ('mame', 1), ('nada', 1), 
	('push', 1), ('prob', 1), ('wild', 1), ('whew', 1), ('dark', 1), ('waht', 1), ('test', 1), ('boot', 1), ('hiom', 1), 
	('HAHA', 1), ('dman', 1), ('jail', 1), ('cops', 1), ('hogs', 1), ('peek', 1), ('MORE', 1), ('TIME', 1), ('loud', 1), 
	('o.k.', 1), ('Sexy', 1), ('Ctrl', 1), ('hots', 1), ('Need', 1), ('frst', 1), ('1200', 1), ('crop', 1), ('bomb', 1), 
	('Pour', 1), ('pour', 1), ('Swim', 1), ('Hard', 1), ('eeek', 1), ('tjhe', 1), ('10th', 1), ('heee', 1), ('peel', 1), 
	('fock', 1), ('Kold', 1), ('exit', 1), ('kold', 1), ('3:45', 1), ('MRIs', 1), ('buff', 1), ('plus', 1), ('tory', 1), 
	('knee', 1), ('OOPS', 1), ('oooh', 1), ('lala', 1), ('fake', 1), ('ssid', 1), ('poot', 1), ('poop', 1), ('bird', 1), 
	('plow', 1), ('thnx', 1), ('card', 1), ('Hugs', 1), ('Lord', 1), ('uyes', 1), ('benz', 1), ('<~~~', 1), ('disc', 1), 
	('LONG', 1), ('Been', 1), ('Will', 1), ('bloe', 1), ('blow', 1), ('hooo', 1), ('thje', 1), ('Jess', 1), ('term', 1), 
	('Tina', 1), ('ooer', 1), ('HALO', 1), ('Awww', 1), ('anal', 1), ('Drop', 1), ('dojn', 1), ('wubs', 1), ('mkay', 1), 
	('spat', 1), ('gees', 1), ('hawT', 1), ('yes.', 1), ('puts', 1), ('fish', 1), ('size', 1), ('39.3', 1), ('1980', 1), 
	('64.8', 1), ('syck', 1), ('tere', 1), ('U542', 1), ('sent', 1), ('45.5', 1), ('98.5', 1), ('1299', 1), ('1900', 1), 
	('1930', 1), ('Werd', 1), ('Rofl', 1), ('mode', 1), ('nawt', 1), ('sign', 1), ('woof', 1), ('sum1', 1), ('ghet', 1), 
	('brad', 1), ('offa', 1), ('Dood', 1), ('out.', 1), ('LOUD', 1), ('sink', 1), ('FINE', 1), ('cums', 1), ('loss', 1), 
	('Life', 1), ('Damn', 1), ('wrap', 1), ('hide', 1), ("PM's", 1), ('Talk', 1), ('okey', 1), ('worl', 1), ('Hold', 1), 
	('cepn', 1), ('lots', 1), ('Mary', 1), ('nawp', 1), ('addy', 1), ('lake', 1), ('slip', 1), ('mite', 1), ('wood', 1), 
	('orta', 1), ('wins', 1), ('ebay', 1), ('coem', 1), ('giva', 1), ('1.98', 1), ('ally', 1), ('Judy', 1), ('cyas', 1), 
	('shup', 1), ('tooo', 1), ("pm'n", 1), ('choc', 1), ('wher', 1), ('whoo', 1), ('dint', 1), ('tend', 1), ('menu', 1), 
	('lust', 1), ('nods', 1), ('NAME', 1), ('kept', 1), ('scuk', 1), ('raed', 1), ('Then', 1), ('bugs', 1), ('nerd', 1), 
	('Hill', 1), ('Evil', 1), ('saME', 1), ('2Pac', 1), ('Time', 1), ('pimp', 1), ('haaa', 1), ('98.6', 1), ("it's", 1), 
	('Mono', 1), ('mono', 1), ('Bone', 1), ('Hero', 1), ('Came', 1), ('.op.', 1), ('Hott', 1), ('Joey', 1), ('Jane', 1), 
	('span', 1), ('wore', 1), ('QUIT', 1), ('pasa', 1), ('barn', 1), ('Kick', 1), ('feat', 1), ('Back', 1), ('dork', 1), 
	('laid', 1), ('Home', 1), ('herd', 1), ('Born', 1), ('Away', 1), ('Tide', 1), ('jush', 1), ('Cute', 1), ('GrlZ', 1), 
	('lung', 1), ('SOME', 1), ('Lion', 1), ('brat', 1), (':o *', 1), ('MUAH', 1), ('fawk', 1), ('dust', 1), ('Help', 1), 
	('seth', 1), ('Heya', 1), ('bone', 1), ('abou', 1), ('tthe', 1), ('Even', 1), ('herE', 1), ('Hail', 1), ('halo', 1), 
	('pork', 1), ('1cos', 1), ("yw's", 1), ('mark', 1), ('dotn', 1), ('PMSL', 1), ('pmsl', 1), ('gift', 1), ('outs', 1), 
	('Paul', 1), ('outa', 1), ('York', 1), ('Care', 1), ('Chat', 1), ('fear', 1), ('dies', 1), ('givs', 1), ('bust', 1), 
	('xmas', 1), ('enuf', 1), ('LoVe', 1), ('eeww', 1), ('dick', 1), ('fair', 1), ('lyin', 1), ('lois', 1), ('cuss', 1), 
	('LATE', 1), ('THEY', 1), ('GOOD', 1), ('rape', 1), ('geez', 1), ('tart', 1), ('hgey', 1), ('caan', 1), ('lol.', 1), 
	('Elle', 1), ('nude', 1), ('allo', 1), ('yesh', 1), ('wind', 1), ('Reub', 1), ('!???', 1), ('heat', 1), ('kmph', 1), 
	('pope', 1), ('yess', 1), ('!...', 1), ('duet', 1), ('wuts', 1), ('west', 1), ('quiz', 1), ('scar', 1), ('Girl', 1), 
	('pair', 1), ('Rang', 1), ('rang', 1), ('bell', 1), ('dawg', 1), ('febe', 1), ('Prof', 1), ('Kewl', 1), ('jude', 1), 
	('Yoko', 1), ('seee', 1), ('whou', 1), ('idnt', 1), ('perk', 1), ('http', 1), ('2DAY', 1), ('yell', 1), ('mang', 1), 
	('SSRI', 1), ('cure', 1), ('wean', 1), ('post', 1), ('anti', 1), ('noth', 1), ('tall', 1), ('pray', 1), ('weed', 1), 
	('icky', 1), ('Rick', 1), ('spit', 1), ('lube', 1), ('mami', 1), ('east', 1), ('18ST', 1), ('seat', 1), ('cock', 1), 
	('SExy', 1), ('otay', 1), ('firs', 1), ('site', 1), ('U113', 1), ('dump', 1), ('toop', 1), ('four', 1), ('U118', 1), 
	('sets', 1), ('asss', 1), ('paid', 1), ('Iowa', 1), ('Teck', 1), ('"...', 1), ('jeff', 1), ('crib', 1), ('drug', 1), 
	('cook', 1), ('9:10', 1), ('ladz', 1), ('aime', 1), ('hong', 1), ('kong', 1), ('Oops', 1), ('tits', 1), ('gret', 1), 
	('guns', 1), ('inch', 1), ('sean', 1), ('howl', 1), ('Take', 1), ('z-ro', 1), ('U137', 1), ('Haha', 1), ('1985', 1), 
	('slam', 1), ('pine', 1), ('puke', 1), ('waaa', 1), ('urls', 1), ('star', 1), ('Save', 1), ('teck', 1), ('Room', 1), 
	('sori', 1), ('Long', 1), ('poem', 1), ('jack', 1), ('Rule', 1), ('CAPS', 1), ('junk', 1), ('tips', 1), ('rush', 1), 
	('Nooo', 1), ('Troy', 1), ('tail', 1), ('Seee', 1), ('6:38', 1), ('dyed', 1), ('t he', 1), ('beam', 1), ('daft', 1), 
	('twit', 1), ('scum', 1), ('U134', 1), ('Type', 1), ('WHOA', 1), ('toke', 1), ('ribs', 1), ('Eggs', 1), ('Wyte', 1), 
	('moms', 1), ('Over', 1), ('West', 1), ('Rock', 1), ('goof', 1), ('U143', 1), ('able', 1), ('vamp', 1), ('Nope', 1), 
	('Kent', 1), ('ther', 1), ('U147', 1), ('TEXT', 1), ('SIZE', 1), ('gear', 1), ('CALI', 1), ('Matt', 1), ('Rush', 1), 
	('AWAY', 1), ('NTMN', 1), ('Kiss', 1), ('U158', 1), ('grea', 1), ('Look', 1), ('guts', 1), ('wrek', 1), ('Fort', 1), 
	('2:55', 1), ('AKST', 1), ('4:03', 1), ('wire', 1), ('soda', 1), ('gray', 1), ('tlak', 1), ('ltnc', 1), ("ok'd", 1), 
	('sayn', 1), ('evah', 1), ('bike', 1), ('hill', 1), ('ohwa', 1), ('caca', 1), ('prep', 1), ('pull', 1), ('dirt', 1), 
	('vent', 1), ('100%', 1), ('safe', 1), ('dogs', 1), ('bull', 1), ('asks', 1), ('Road', 1), ('chit', 1), ('grin', 1), 
	('bred', 1), ('rats', 1), ('Sat.', 1), ('samn', 1), ('Phil', 1), ('nuff', 1), ('rose', 1), ('Ruth', 1), ('grew', 1), 
	('mena', 1), ('ROFL', 1), ('lapd', 1), ('surf', 1), ('City', 1), ('hazy', 1), ('thot', 1), ('acid', 1), ('wide', 1), 
	('keys', 1), ('salt', 1), ('mess', 1), ('base', 1), ('byes', 1), ("RN's", 1), ('yout', 1), ('numb', 1), ('thah', 1), 
	('mahn', 1), ('King', 1), ('TALK', 1), ('GIRL', 1), ('WHEN', 1), ('HOTT', 1), ('HERE', 1), ('soup', 1), ('6:51', 1), 
	('9.53', 1), ('Mine', 1), ('vega', 1), ('pigs', 1), ('king', 1), ('poof', 1), ('Nova', 1), ('mofo', 1), ('Ohhh', 1), 
	('Holy', 1), ('sips', 1), ('clay', 1), ('None', 1), ('Male', 1), ('bacl', 1), ('body', 1), ('akon', 1), ('yoll', 1), 
	('boom', 1), ('News', 1), ('Maps', 1), ('page', 1), ('Tiff', 1), ('Chop', 1), ('DAMN', 1), ('TYPR', 1), ('poll', 1), 
	('boed', 1), ('Dude', 1), ('Does', 1), ('pwns', 1), ('Very', 1), ('Good', 1), ('Food', 1), ('sexi', 1), ('bois', 1), 
	('KNOW', 1), ('GUYS', 1), ('YALL', 1), ('EVEN', 1), ('SEEN', 1), ('WILL', 1), ('COME', 1), ('FACE', 1), ('JUST', 1), 
	('Kids', 1), ('6:41', 1), ('bied', 1), ('6:53', 1), ('U149', 1), ('7:45', 1), ('Uhhh', 1), ('tenn', 1), ('pure', 1), 
	('U164', 1), ('U150', 1), ('U181', 1), ('gals', 1), ('woah', 1), ('ussy', 1), ('tiff', 1), ('Heys', 1), ("<3's", 1), 
	('lisa', 1), ('brwn', 1), ('hurr', 1), ('Were', 1)]
23. below put into a list for the sake of space
	['SCENE', 'KING', 'ARTHUR', 'SOLDIER', 'ARTHUR', 'I', 'SOLDIER', 'ARTHUR', 'I', 'I', 'SOLDIER', 'ARTHUR', 'SOLDIER', 
	'ARTHUR', 'SOLDIER', 'ARTHUR', 'SOLDIER', 'ARTHUR', 'SOLDIER', 'ARTHUR', 'SOLDIER', 'ARTHUR', 'SOLDIER', 'ARTHUR', 
	'SOLDIER', 'A', 'ARTHUR', 'SOLDIER', 'A', 'ARTHUR', 'SOLDIER', 'ARTHUR', 'SOLDIER', 'I', 'ARTHUR', 'I', 'SOLDIER', 
	'SOLDIER', 'SOLDIER', 'I', 'ARTHUR', 'SOLDIER', 'SOLDIER', 'SOLDIER', 'SOLDIER', 'SOLDIER', 'SOLDIER', 'SOLDIER', 
	'SOLDIER', 'SCENE', 'CART', 'MASTER', 'CUSTOMER', 'CART', 'MASTER', 'DEAD', 'PERSON', 'I', 'CART', 'MASTER', 
	'CUSTOMER', 'DEAD', 'PERSON', 'I', 'CART', 'MASTER', 'CUSTOMER', 'DEAD', 'PERSON', 'I', 'CART', 'MASTER', 'CUSTOMER', 
	'DEAD', 'PERSON', 'I', 'CUSTOMER', 'CART', 'MASTER', 'I', 'DEAD', 'PERSON', 'I', 'CUSTOMER', 'CART', 'MASTER', 'I', 
	'DEAD', 'PERSON', 'I', 'CUSTOMER', 'CART', 'MASTER', 'I', 'CUSTOMER', 'CART', 'MASTER', 'I', 'CUSTOMER', 'CART', 
	'MASTER', 'DEAD', 'PERSON', 'I', 'I', 'CUSTOMER', 'DEAD', 'PERSON', 'I', 'I', 'CUSTOMER', 'CART', 'MASTER', 'CUSTOMER', 
	'CART', 'MASTER', 'I', 'CUSTOMER', 'CART', 'MASTER', 'SCENE', 'ARTHUR', 'DENNIS', 'ARTHUR', 'DENNIS', 'I', 'ARTHUR', 
	'I', 'DENNIS', 'I', 'I', 'ARTHUR', 'I', 'DENNIS', 'ARTHUR', 'I', 'DENNIS', 'ARTHUR', 'I', 'DENNIS', 'I', 'ARTHUR', 'I', 
	'DENNIS', 'WOMAN', 'ARTHUR', 'I', 'WOMAN', 'ARTHUR', 'WOMAN', 'ARTHUR', 'I', 'WOMAN', 'I', 'I', 'DENNIS', 'A', 'WOMAN', 
	'DENNIS', 'ARTHUR', 'I', 'WOMAN', 'ARTHUR', 'WOMAN', 'ARTHUR', 'DENNIS', 'I', 'ARTHUR', 'DENNIS', 'ARTHUR', 'I', 'DENNIS', 
	'ARTHUR', 'DENNIS', 'ARTHUR', 'I', 'WOMAN', 'ARTHUR', 'I', 'WOMAN', 'I', 'ARTHUR', 'WOMAN', 'ARTHUR', 'I', 'I', 'DENNIS', 
	'ARTHUR', 'DENNIS', 'ARTHUR', 'DENNIS', 'I', 'I', 'I', 'ARTHUR', 'DENNIS', 'ARTHUR', 'DENNIS', 'I', 'ARTHUR', 'DENNIS', 'I', 
	'SCENE', 'BLACK', 'KNIGHT', 'BLACK', 'KNIGHT', 'GREEN', 'KNIGHT', 'BLACK', 'KNIGHT', 'GREEN', 'KNIGHT', 'BLACK', 'KNIGHT', 
	'BLACK', 'KNIGHT', 'GREEN', 'KNIGHT', 'GREEN', 'KNIGHT', 'BLACK', 'KNIGHT', 'GREEN', 'KNIGHT', 'BLACK', 'KNIGHT', 'ARTHUR', 
	'I', 'I', 'BLACK', 'KNIGHT', 'ARTHUR', 'BLACK', 'KNIGHT', 'ARTHUR', 'I', 'I', 'BLACK', 'KNIGHT', 'ARTHUR', 'I', 'BLACK', 
	'KNIGHT', 'I', 'ARTHUR', 'ARTHUR', 'BLACK', 'KNIGHT', 'ARTHUR', 'BLACK', 'KNIGHT', 'ARTHUR', 'BLACK', 'KNIGHT', 'ARTHUR', 
	'A', 'BLACK', 'KNIGHT', 'ARTHUR', 'BLACK', 'KNIGHT', 'I', 'ARTHUR', 'BLACK', 'KNIGHT', 'ARTHUR', 'BLACK', 'KNIGHT', 'ARTHUR', 
	'BLACK', 'KNIGHT', 'ARTHUR', 'BLACK', 'KNIGHT', 'ARTHUR', 'BLACK', 'KNIGHT', 'ARTHUR', 'BLACK', 'KNIGHT', 'I', 'ARTHUR', 
	'BLACK', 'KNIGHT', 'ARTHUR', 'BLACK', 'KNIGHT', 'ARTHUR', 'I', 'ARTHUR', 'BLACK', 'KNIGHT', 'BLACK', 'KNIGHT', 'I', 'ARTHUR', 
	'BLACK', 'KNIGHT', 'ARTHUR', 'BLACK', 'KNIGHT', 'I', 'ARTHUR', 'BLACK', 'KNIGHT', 'ARTHUR', 'BLACK', 'KNIGHT', 'BLACK', 
	'KNIGHT', 'ARTHUR', 'BLACK', 'KNIGHT', 'I', 'I', 'SCENE', 'MONKS', 'CROWD', 'A', 'A', 'A', 'A', 'MONKS', 'CROWD', 'A', 'A', 
	'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'VILLAGER', 'CROWD', 'BEDEVERE', 'VILLAGER', 'CROWD', 'BEDEVERE', 
	'WITCH', 'I', 'I', 'BEDEVERE', 'WITCH', 'CROWD', 'WITCH', 'BEDEVERE', 'VILLAGER', 'BEDEVERE', 'VILLAGER', 'VILLAGER', 'CROWD', 
	'BEDEVERE', 'VILLAGER', 'VILLAGER', 'VILLAGER', 'VILLAGER', 'VILLAGERS', 'VILLAGER', 'VILLAGER', 'VILLAGER', 'VILLAGER', 'A', 
	'VILLAGERS', 'A', 'VILLAGER', 'A', 'VILLAGER', 'RANDOM', 'BEDEVERE', 'VILLAGER', 'BEDEVERE', 'A', 'VILLAGER', 'I', 'VILLAGER', 
	'VILLAGER', 'CROWD', 'BEDEVERE', 'VILLAGER', 'VILLAGER', 'VILLAGER', 'CROWD', 'BEDEVERE', 'VILLAGER', 'VILLAGER', 'CROWD', 
	'BEDEVERE', 'VILLAGER', 'VILLAGER', 'VILLAGER', 'BEDEVERE', 'VILLAGER', 'B', 'BEDEVERE', 'CROWD', 'BEDEVERE', 'VILLAGER', 
	'BEDEVERE', 'VILLAGER', 'RANDOM', 'BEDEVERE', 'VILLAGER', 'VILLAGER', 'VILLAGER', 'CROWD', 'BEDEVERE', 'VILLAGER', 'VILLAGER', 
	'VILLAGER', 'VILLAGER', 'VILLAGER', 'VILLAGER', 'VILLAGER', 'VILLAGER', 'VILLAGER', 'ARTHUR', 'A', 'CROWD', 'BEDEVERE', 
	'VILLAGER', 'BEDEVERE', 'VILLAGER', 'A', 'VILLAGER', 'A', 'CROWD', 'A', 'A', 'VILLAGER', 'BEDEVERE', 'CROWD', 'BEDEVERE', 
	'CROWD', 'A', 'A', 'A', 'WITCH', 'VILLAGER', 'CROWD', 'BEDEVERE', 'ARTHUR', 'I', 'BEDEVERE', 'ARTHUR', 'BEDEVERE', 'I', 'ARTHUR', 
	'BEDEVERE', 'ARTHUR', 'I', 'NARRATOR', 'SCENE', 'SIR', 'BEDEVERE', 'ARTHUR', 'BEDEVERE', 'SIR', 'LAUNCELOT', 'ARTHUR', 'SIR', 
	'GALAHAD', 'LAUNCELOT', 'PATSY', 'ARTHUR', 'I', 'KNIGHTS', 'PRISONER', 'KNIGHTS', 'MAN', 'I', 'ARTHUR', 'KNIGHTS', 'SCENE', 
	'GOD', 'I', 'ARTHUR', 'GOD', 'I', 'I', 'ARTHUR', 'I', 'O', 'GOD', 'ARTHUR', 'GOD', 'ARTHUR', 'O', 'GOD', 'LAUNCELOT', 'A', 'A', 
	'GALAHAD', 'SCENE', 'ARTHUR', 'FRENCH', 'GUARD', 'ARTHUR', 'FRENCH', 'GUARD', 'ARTHUR', 'FRENCH', 'GUARD', 'I', 'I', 'ARTHUR', 
	'GALAHAD', 'ARTHUR', 'FRENCH', 'GUARD', 'I', 'ARTHUR', 'FRENCH', 'GUARD', 'ARTHUR', 'FRENCH', 'GUARD', 'I', 'I', 'GALAHAD', 
	'FRENCH', 'GUARD', 'ARTHUR', 'FRENCH', 'GUARD', 'I', 'GALAHAD', 'ARTHUR', 'FRENCH', 'GUARD', 'I', 'I', 'GALAHAD', 'FRENCH', 
	'GUARD', 'I', 'ARTHUR', 'I', 'FRENCH', 'GUARD', 'OTHER', 'FRENCH', 'GUARD', 'FRENCH', 'GUARD', 'ARTHUR', 'I', 'KNIGHTS', 'ARTHUR', 
	'KNIGHTS', 'FRENCH', 'GUARD', 'FRENCH', 'GUARD', 'ARTHUR', 'KNIGHTS', 'FRENCH', 'GUARD', 'FRENCH', 'GUARDS', 'LAUNCELOT', 'I', 
	'ARTHUR', 'BEDEVERE', 'I', 'FRENCH', 'GUARDS', 'C', 'A', 'ARTHUR', 'BEDEVERE', 'I', 'ARTHUR', 'BEDEVERE', 'U', 'I', 'ARTHUR', 
	'BEDEVERE', 'ARTHUR', 'KNIGHTS', 'CRASH', 'FRENCH', 'GUARDS', 'SCENE', 'VOICE', 'DIRECTOR', 'HISTORIAN', 'KNIGHT', 'KNIGHT', 
	'HISTORIAN', 'HISTORIAN', 'S', 'WIFE', 'SCENE', 'NARRATOR', 'MINSTREL', 'O', 'SIR', 'ROBIN', 'DENNIS', 'WOMAN', 'ALL', 'HEADS', 
	'MINSTREL', 'ROBIN', 'I', 'ALL', 'HEADS', 'MINSTREL', 'ROBIN', 'I', 'ALL', 'HEADS', 'I', 'ROBIN', 'W', 'I', 'I', 'ALL', 'HEADS', 
	'ROBIN', 'I', 'LEFT', 'HEAD', 'I', 'MIDDLE', 'HEAD', 'I', 'RIGHT', 'HEAD', 'I', 'MIDDLE', 'HEAD', 'I', 'LEFT', 'HEAD', 'I', 'RIGHT', 
	'HEAD', 'LEFT', 'HEAD', 'ROBIN', 'I', 'LEFT', 'HEAD', 'I', 'RIGHT', 'HEAD', 'MIDDLE', 'HEAD', 'LEFT', 'HEAD', 'RIGHT', 'HEAD', 
	'MIDDLE', 'HEAD', 'LEFT', 'HEAD', 'MIDDLE', 'HEAD', 'LEFT', 'HEAD', 'I', 'MIDDLE', 'HEAD', 'RIGHT', 'HEAD', 'LEFT', 'HEAD', 'MIDDLE', 
	'HEAD', 'RIGHT', 'HEAD', 'LEFT', 'HEAD', 'ALL', 'HEADS', 'MIDDLE', 'HEAD', 'RIGHT', 'HEAD', 'MINSTREL', 'ROBIN', 'MINSTREL', 'ROBIN', 
	'I', 'MINSTREL', 'ROBIN', 'MINSTREL', 'ROBIN', 'I', 'MINSTREL', 'ROBIN', 'I', 'MINSTREL', 'ROBIN', 'MINSTREL', 'ROBIN', 'I', 
	'CARTOON', 'MONKS', 'CARTOON', 'CHARACTER', 'CARTOON', 'MONKS', 'CARTOON', 'CHARACTERS', 'CARTOON', 'MONKS', 'CARTOON', 'CHARACTER', 
	'VOICE', 'CARTOON', 'CHARACTER', 'SCENE', 'NARRATOR', 'GALAHAD', 'GIRLS', 'ZOOT', 'GALAHAD', 'ZOOT', 'GALAHAD', 'ZOOT', 'GALAHAD', 
	'ZOOT', 'MIDGET', 'CRAPPER', 'O', 'ZOOT', 'MIDGET', 'CRAPPER', 'ZOOT', 'GALAHAD', 'I', 'I', 'ZOOT', 'GALAHAD', 'ZOOT', 'GALAHAD', 
	'ZOOT', 'GALAHAD', 'I', 'ZOOT', 'GALAHAD', 'I', 'I', 'ZOOT', 'I', 'GALAHAD', 'ZOOT', 'PIGLET', 'GALAHAD', 'ZOOT', 'GALAHAD', 'B', 
	'ZOOT', 'WINSTON', 'GALAHAD', 'PIGLET', 'GALAHAD', 'PIGLET', 'GALAHAD', 'I', 'PIGLET', 'GALAHAD', 'I', 'PIGLET', 'GALAHAD', 'I', 
	'I', 'I', 'GIRLS', 'GALAHAD', 'GIRLS', 'GALAHAD', 'DINGO', 'I', 'GALAHAD', 'I', 'DINGO', 'GALAHAD', 'I', 'I', 'DINGO', 'GALAHAD', 
	'DINGO', 'I', 'GALAHAD', 'DINGO', 'I', 'LEFT', 'HEAD', 'DENNIS', 'OLD', 'MAN', 'TIM', 'THE', 'ENCHANTER', 'ARMY', 'OF', 'KNIGHTS', 
	'DINGO', 'I', 'GOD', 'DINGO', 'GIRLS', 'A', 'A', 'DINGO', 'AMAZING', 'STUNNER', 'LOVELY', 'DINGO', 'GIRLS', 'A', 'A', 'DINGO', 
	'GIRLS', 'GALAHAD', 'I', 'LAUNCELOT', 'GALAHAD', 'LAUNCELOT', 'GALAHAD', 'LAUNCELOT', 'GALAHAD', 'LAUNCELOT', 'DINGO', 'LAUNCELOT', 
	'GALAHAD', 'LAUNCELOT', 'GALAHAD', 'I', 'LAUNCELOT', 'GIRLS', 'GALAHAD', 'I', 'DINGO', 'GIRLS', 'LAUNCELOT', 'GALAHAD', 'I', 'I', 
	'DINGO', 'GIRLS', 'LAUNCELOT', 'GALAHAD', 'I', 'DINGO', 'GIRLS', 'DINGO', 'LAUNCELOT', 'GALAHAD', 'I', 'I', 'LAUNCELOT', 'GALAHAD', 
	'LAUNCELOT', 'GALAHAD', 'I', 'LAUNCELOT', 'GALAHAD', 'LAUNCELOT', 'GALAHAD', 'I', 'LAUNCELOT', 'I', 'NARRATOR', 'I', 'I', 'CROWD', 
	'NARRATOR', 'I', 'SCENE', 'OLD', 'MAN', 'ARTHUR', 'OLD', 'MAN', 'ARTHUR', 'OLD', 'MAN', 'ARTHUR', 'OLD', 'MAN', 'ARTHUR', 'OLD', 'MAN', 
	'ARTHUR', 'OLD', 'MAN', 'ARTHUR', 'OLD', 'MAN', 'SCENE', 'HEAD', 'KNIGHT', 'OF', 'NI', 'KNIGHTS', 'OF', 'NI', 'ARTHUR', 'HEAD', 'KNIGHT', 
	'RANDOM', 'ARTHUR', 'HEAD', 'KNIGHT', 'BEDEVERE', 'HEAD', 'KNIGHT', 'RANDOM', 'ARTHUR', 'HEAD', 'KNIGHT', 'ARTHUR', 'HEAD', 'KNIGHT', 
	'KNIGHTS', 'OF', 'NI', 'ARTHUR', 'HEAD', 'KNIGHT', 'ARTHUR', 'HEAD', 'KNIGHT', 'ARTHUR', 'A', 'KNIGHTS', 'OF', 'NI', 'ARTHUR', 'PARTY', 
	'ARTHUR', 'HEAD', 'KNIGHT', 'ARTHUR', 'O', 'HEAD', 'KNIGHT', 'ARTHUR', 'HEAD', 'KNIGHT', 'ARTHUR', 'HEAD', 'KNIGHT', 'CARTOON', 
	'CHARACTER', 'SUN', 'CARTOON', 'CHARACTER', 'SUN', 'CARTOON', 'CHARACTER', 'SUN', 'CARTOON', 'CHARACTER', 'SCENE', 'NARRATOR', 'FATHER', 
	'PRINCE', 'HERBERT', 'FATHER', 'HERBERT', 'FATHER', 'HERBERT', 'B', 'I', 'FATHER', 'I', 'I', 'I', 'I', 'I', 'I', 'HERBERT', 'I', 'I', 
	'FATHER', 'HERBERT', 'I', 'FATHER', 'I', 'HERBERT', 'B', 'I', 'FATHER', 'HERBERT', 'FATHER', 'HERBERT', 'I', 'FATHER', 'HERBERT', 'I', 
	'I', 'I', 'FATHER', 'I', 'GUARD', 'GUARD', 'FATHER', 'I', 'GUARD', 'FATHER', 'GUARD', 'GUARD', 'FATHER', 'GUARD', 'FATHER', 'GUARD', 
	'FATHER', 'GUARD', 'GUARD', 'FATHER', 'GUARD', 'FATHER', 'GUARD', 'FATHER', 'GUARD', 'FATHER', 'GUARD', 'FATHER', 'GUARD', 'I', 'FATHER', 
	'N', 'GUARD', 'FATHER', 'GUARD', 'FATHER', 'GUARD', 'GUARD', 'FATHER', 'GUARD', 'FATHER', 'GUARD', 'GUARD', 'FATHER', 'GUARD', 'FATHER', 
	'GUARD', 'FATHER', 'GUARD', 'GUARD', 'GUARD', 'I', 'FATHER', 'GUARD', 'GUARD', 'FATHER', 'GUARD', 'FATHER', 'I', 'GUARD', 'I', 'HERBERT', 
	'FATHER', 'GUARD', 'FATHER', 'SCENE', 'LAUNCELOT', 'CONCORDE', 'LAUNCELOT', 'CONCORDE', 'LAUNCELOT', 'I', 'I', 'A', 'A', 'CONCORDE', 'I', 
	'I', 'LAUNCELOT', 'CONCORDE', 'I', 'I', 'I', 'I', 'I', 'LAUNCELOT', 'I', 'CONCORDE', 'I', 'I', 'LAUNCELOT', 'I', 'I', 'CONCORDE', 
	'LAUNCELOT', 'CONCORDE', 'I', 'LAUNCELOT', 'CONCORDE', 'I', 'I', 'I', 'SCENE', 'PRINCESS', 'LUCKY', 'GIRLS', 'GUEST', 'SENTRY', 'SENTRY', 
	'SENTRY', 'LAUNCELOT', 'SENTRY', 'LAUNCELOT', 'PRINCESS', 'LUCKY', 'GIRLS', 'LAUNCELOT', 'GUESTS', 'LAUNCELOT', 'GUARD', 'LAUNCELOT', 'O', 
	'I', 'I', 'HERBERT', 'LAUNCELOT', 'I', 'I', 'HERBERT', 'LAUNCELOT', 'I', 'HERBERT', 'I', 'I', 'LAUNCELOT', 'I', 'HERBERT', 'FATHER', 
	'HERBERT', 'I', 'FATHER', 'LAUNCELOT', 'I', 'HERBERT', 'LAUNCELOT', 'FATHER', 'LAUNCELOT', 'FATHER', 'LAUNCELOT', 'I', 'I', 'HERBERT', 
	'I', 'FATHER', 'LAUNCELOT', 'I', 'FATHER', 'I', 'HERBERT', 'FATHER', 'LAUNCELOT', 'I', 'FATHER', 'LAUNCELOT', 'FATHER', 'LAUNCELOT', 'I', 
	'I', 'I', 'FATHER', 'HERBERT', 'LAUNCELOT', 'I', 'FATHER', 'LAUNCELOT', 'HERBERT', 'I', 'FATHER', 'LAUNCELOT', 'HERBERT', 'I', 'LAUNCELOT', 
	'I', 'HERBERT', 'LAUNCELOT', 'I', 'I', 'I', 'FATHER', 'HERBERT', 'SCENE', 'GUESTS', 'FATHER', 'GUEST', 'FATHER', 'LAUNCELOT', 'FATHER', 
	'LAUNCELOT', 'I', 'I', 'I', 'GUEST', 'GUESTS', 'FATHER', 'LAUNCELOT', 'GUEST', 'GUESTS', 'FATHER', 'GUESTS', 'FATHER', 'I', 'I', 'GUEST', 
	'FATHER', 'GUEST', 'FATHER', 'BRIDE', 'S', 'FATHER', 'GUEST', 'FATHER', 'I', 'I', 'LAUNCELOT', 'GUEST', 'GUESTS', 'CONCORDE', 'HERBERT', 
	'I', 'FATHER', 'HERBERT', 'I', 'FATHER', 'HERBERT', 'I', 'FATHER', 'GUESTS', 'FATHER', 'GUESTS', 'FATHER', 'GUESTS', 'FATHER', 'GUESTS', 
	'FATHER', 'GUESTS', 'CONCORDE', 'GUESTS', 'CONCORDE', 'GUESTS', 'LAUNCELOT', 'GUESTS', 'LAUNCELOT', 'I', 'GUESTS', 'CONCORDE', 'LAUNCELOT', 
	'GUESTS', 'LAUNCELOT', 'GUESTS', 'LAUNCELOT', 'SCENE', 'ARTHUR', 'OLD', 'CRONE', 'ARTHUR', 'CRONE', 'ARTHUR', 'I', 'CRONE', 'ARTHUR', 
	'CRONE', 'ARTHUR', 'CRONE', 'BEDEVERE', 'ARTHUR', 'BEDEVERE', 'ARTHUR', 'BEDEVERE', 'ARTHUR', 'BEDEVERE', 'ARTHUR', 'BEDEVERE', 'ARTHUR', 
	'ARTHUR', 'BEDEVERE', 'CRONE', 'BEDEVERE', 'ARTHUR', 'CRONE', 'BEDEVERE', 'ARTHUR', 'BEDEVERE', 'ARTHUR', 'BEDEVERE', 'ROGER', 'THE', 
	'SHRUBBER', 'ARTHUR', 'ROGER', 'ARTHUR', 'ROGER', 'I', 'I', 'BEDEVERE', 'ARTHUR', 'SCENE', 'ARTHUR', 'O', 'HEAD', 'KNIGHT', 'I', 'ARTHUR', 
	'HEAD', 'KNIGHT', 'KNIGHTS', 'OF', 'NI', 'HEAD', 'KNIGHT', 'RANDOM', 'HEAD', 'KNIGHT', 'ARTHUR', 'O', 'HEAD', 'KNIGHT', 'ARTHUR', 'RANDOM', 
	'HEAD', 'KNIGHT', 'KNIGHTS', 'OF', 'NI', 'A', 'A', 'A', 'HEAD', 'KNIGHT', 'ARTHUR', 'HEAD', 'KNIGHT', 'ARTHUR', 'KNIGHTS', 'OF', 'NI', 
	'HEAD', 'KNIGHT', 'ARTHUR', 'HEAD', 'KNIGHT', 'I', 'ARTHUR', 'KNIGHTS', 'OF', 'NI', 'HEAD', 'KNIGHT', 'ARTHUR', 'KNIGHTS', 'OF', 'NI', 'HEAD', 
	'KNIGHT', 'KNIGHTS', 'OF', 'NI', 'BEDEVERE', 'MINSTREL', 'ARTHUR', 'ROBIN', 'HEAD', 'KNIGHT', 'ARTHUR', 'MINSTREL', 'ROBIN', 'HEAD', 'KNIGHT', 
	'KNIGHTS', 'OF', 'NI', 'ROBIN', 'I', 'KNIGHTS', 'OF', 'NI', 'ROBIN', 'ARTHUR', 'KNIGHTS', 'OF', 'NI', 'HEAD', 'KNIGHT', 'ARTHUR', 'KNIGHTS', 
	'OF', 'NI', 'HEAD', 'KNIGHT', 'ARTHUR', 'HEAD', 'KNIGHT', 'I', 'I', 'I', 'KNIGHTS', 'OF', 'NI', 'NARRATOR', 'KNIGHTS', 'NARRATOR', 'MINSTREL', 
	'NARRATOR', 'KNIGHTS', 'NARRATOR', 'A', 'CARTOON', 'CHARACTER', 'NARRATOR', 'CARTOON', 'CHARACTER', 'NARRATOR', 'CARTOON', 'CHARACTER', 
	'NARRATOR', 'CARTOON', 'CHARACTER', 'NARRATOR', 'CARTOON', 'CHARACTER', 'NARRATOR', 'SCENE', 'KNIGHTS', 'ARTHUR', 'TIM', 'THE', 'ENCHANTER', 
	'I', 'ARTHUR', 'TIM', 'ARTHUR', 'TIM', 'ARTHUR', 'TIM', 'I', 'ARTHUR', 'O', 'TIM', 'ROBIN', 'ARTHUR', 'KNIGHTS', 'ARTHUR', 'BEDEVERE', 
	'GALAHAD', 'ROBIN', 'BEDEVERE', 'ROBIN', 'BEDEVERE', 'ARTHUR', 'GALAHAD', 'ARTHUR', 'I', 'I', 'TIM', 'A', 'ARTHUR', 'A', 'TIM', 'A', 
	'ARTHUR', 'I', 'ROBIN', 'Y', 'ARTHUR', 'GALAHAD', 'KNIGHTS', 'TIM', 'ROBIN', 'ARTHUR', 'ROBIN', 'GALAHAD', 'ARTHUR', 'ROBIN', 'KNIGHTS', 
	'ARTHUR', 'TIM', 'I', 'KNIGHTS', 'TIM', 'ARTHUR', 'O', 'TIM', 'ARTHUR', 'SCENE', 'GALAHAD', 'ARTHUR', 'TIM', 'ARTHUR', 'GALAHAD', 'ARTHUR', 
	'W', 'TIM', 'ARTHUR', 'TIM', 'ARTHUR', 'TIM', 'ARTHUR', 'TIM', 'ARTHUR', 'TIM', 'ARTHUR', 'TIM', 'ARTHUR', 'TIM', 'ROBIN', 'I', 'I', 'TIM', 
	'GALAHAD', 'TIM', 'GALAHAD', 'ROBIN', 'TIM', 'I', 'ROBIN', 'TIM', 'ARTHUR', 'BORS', 'TIM', 'BORS', 'ARTHUR', 'TIM', 'I', 'ROBIN', 'I', 'TIM', 
	'I', 'I', 'ARTHUR', 'TIM', 'ARTHUR', 'TIM', 'KNIGHTS', 'KNIGHTS', 'ARTHUR', 'KNIGHTS', 'TIM', 'ARTHUR', 'LAUNCELOT', 'GALAHAD', 'ARTHUR', 
	'GALAHAD', 'ARTHUR', 'ROBIN', 'ARTHUR', 'GALAHAD', 'ARTHUR', 'GALAHAD', 'LAUNCELOT', 'ARTHUR', 'LAUNCELOT', 'ARTHUR', 'MONKS', 'ARTHUR', 
	'LAUNCELOT', 'I', 'ARTHUR', 'BROTHER', 'MAYNARD', 'SECOND', 'BROTHER', 'O', 'MAYNARD', 'SECOND', 'BROTHER', 'MAYNARD', 'KNIGHTS', 'ARTHUR', 
	'GALAHAD', 'ARTHUR', 'SCENE', 'ARTHUR', 'LAUNCELOT', 'GALAHAD', 'ARTHUR', 'MAYNARD', 'GALAHAD', 'LAUNCELOT', 'ARTHUR', 'MAYNARD', 'ARTHUR', 
	'MAYNARD', 'BEDEVERE', 'MAYNARD', 'LAUNCELOT', 'MAYNARD', 'ARTHUR', 'MAYNARD', 'GALAHAD', 'ARTHUR', 'MAYNARD', 'LAUNCELOT', 'ARTHUR', 
	'BEDEVERE', 'GALAHAD', 'BEDEVERE', 'I', 'LAUNCELOT', 'ARTHUR', 'LAUNCELOT', 'KNIGHTS', 'BEDEVERE', 'LAUNCELOT', 'BEDEVERE', 'N', 'LAUNCELOT', 
	'BEDEVERE', 'I', 'ARTHUR', 'GALAHAD', 'MAYNARD', 'BROTHER', 'MAYNARD', 'BEDEVERE', 'ARTHUR', 'KNIGHTS', 'BEDEVERE', 'KNIGHTS', 'NARRATOR', 
	'ANIMATOR', 'NARRATOR', 'SCENE', 'GALAHAD', 'ARTHUR', 'ROBIN', 'ARTHUR', 'BEDEVERE', 'ARTHUR', 'GALAHAD', 'ARTHUR', 'GALAHAD', 'ARTHUR', 
	'ROBIN', 'ARTHUR', 'ROBIN', 'I', 'GALAHAD', 'ARTHUR', 'ROBIN', 'ARTHUR', 'ROBIN', 'I', 'LAUNCELOT', 'I', 'I', 'ARTHUR', 'GALAHAD', 'ARTHUR', 
	'LAUNCELOT', 'I', 'ARTHUR', 'BRIDGEKEEPER', 'LAUNCELOT', 'I', 'BRIDGEKEEPER', 'LAUNCELOT', 'BRIDGEKEEPER', 'LAUNCELOT', 'BRIDGEKEEPER', 
	'LAUNCELOT', 'BRIDGEKEEPER', 'LAUNCELOT', 'ROBIN', 'BRIDGEKEEPER', 'ROBIN', 'I', 'BRIDGEKEEPER', 'ROBIN', 'BRIDGEKEEPER', 'ROBIN', 
	'BRIDGEKEEPER', 'ROBIN', 'I', 'BRIDGEKEEPER', 'GALAHAD', 'BRIDGEKEEPER', 'GALAHAD', 'I', 'BRIDGEKEEPER', 'GALAHAD', 'BRIDGEKEEPER', 'ARTHUR', 
	'BRIDGEKEEPER', 'ARTHUR', 'BRIDGEKEEPER', 'ARTHUR', 'BRIDGEKEEPER', 'I', 'I', 'BEDEVERE', 'ARTHUR', 'SCENE', 'ARTHUR', 'BEDEVERE', 'ARTHUR', 
	'BEDEVERE', 'ARTHUR', 'FRENCH', 'GUARD', 'ARTHUR', 'I', 'FRENCH', 'GUARD', 'I', 'I', 'ARTHUR', 'FRENCH', 'GUARD', 'I', 'ARTHUR', 'FRENCH', 
	'GUARDS', 'ARTHUR', 'FRENCH', 'GUARD', 'ARTHUR', 'FRENCH', 'GUARD', 'FRENCH', 'GUARDS', 'ARTHUR', 'BEDEVERE', 'ARTHUR', 'FRENCH', 'GUARDS', 
	'ARTHUR', 'FRENCH', 'GUARDS', 'ARTHUR', 'FRENCH', 'GUARDS', 'ARTHUR', 'ARMY', 'OF', 'KNIGHTS', 'HISTORIAN', 'S', 'WIFE', 'I', 'INSPECTOR', 
	'OFFICER', 'HISTORIAN', 'S', 'WIFE', 'OFFICER', 'INSPECTOR', 'OFFICER', 'BEDEVERE', 'INSPECTOR', 'OFFICER', 'INSPECTOR', 'OFFICER', 'OFFICER', 
	'RANDOM', 'RANDOM', 'OFFICER', 'OFFICER', 'OFFICER', 'OFFICER', 'INSPECTOR', 'OFFICER', 'CAMERAMAN']
24. a: [word for word in text6 if word.endswith("ise")]
	b: [word for word in text6 if "z" in word]
	c: [word for word in text6 if "pt" in word]
	d: [word for word in text6 if word.istitle()] # note: istitle checks if rest of word is lowercase as well (ie. "HEY".istitle() returns false)
25. a: for word in sent:
			if word.startswith("sh"):
				print(word)
	b: for word in sent:
			if len(word) > 4:
				print(word)
26. finds the total length of all the words/individual tokens in a text. You could technically use this to find the average word length of a
	text, but keep in mind that there is also punctuation in the tokenization
27. function below for formatting purposes
	def vocabulary_size(text):
		return len(set(text))
28. function below for formatting purposes
	def percent(word, text):
		return 100 * text.count(word)/len(text)
29. a like expression will return a boolean. Seems like it compares the sizes of the respective sets; might be useful when determining 
	which text has more distinct words




