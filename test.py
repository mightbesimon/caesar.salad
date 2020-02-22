import caesar


#===== tests =====#

quotes = [
 		"Julius Caesar",
		"show you hand",
		"you only live once",
		"secret salad recipe",
		"The West wasn't won on salad.",
		"You don't win friends with salad.",
		"He that sups upon salad, goes not to bed fasting",
		"my salad days, When I was green in judgement, cold in blood.",
		"Salad freshens without enfeebling and fortifies without irritating.",
		"Salad, I can't bear salad. It grows while you're eating it, you know.",
		"Salad is never more appetizing than when served in a large wooden bowl.",
		"It takes four men to dress a salad: a wise man for the salt, a madman for the pepper, a miser for the vinegar, and a spendthrift for the oil.",
		"To remember a successful salad is generally to remember a successful dinner; at all events, the perfect dinner necessarily includes the perfect salad.",
		"There was an Old Person of Fife, Who was greatly disgusted with life; They sang him a ballad, and fed him on salad, Which cured that Old Person of Fife.",
		"To make a good salad is to be a brilliant diplomatist - the problem is entirely the same in both cases. To know how much oil one must mix with one's vinegar.",
		"A number of rare or newly experienced foods have been claimed to be aphrodisiacs. At one time this quality was even ascribed to the tomato. Reflect on that when you are next preparing the family salad.",
		"What we think, we become.",
		"join me at eight by the zoo",
		"Whatever you do, do it well.",
		"W. Shakespeare, Julius Caesar",
		"Die with memories, not dreams.",
		"Love For All, Hatred For None.",
		"So many books, so little time.",
		"All limitations are self-imposed.",
		"Be so good they can’t ignore you.",
		"Every moment is a fresh beginning.",
		"Aspire to inspire before we expire.",
		"Change the world by being yourself.",
		"Everything you can imagine is real.",
		"Reality is wrong, dreams are for real.",
		"Yesterday you said tomorrow. Just do it.",
		"Never regret anything that made you smile.",
		"Simplicity is the ultimate sophistication.",
		"Tough times never last but tough people do.",
		"Be yourself; everyone else is already taken.",
		"Determine your priorities and focus on them.",
		"Don’t you know your imperfections is a blessing?",
		"Problems are not stop signs, they are guidelines.",
		"I could agree with you but then we’d both be wrong.",
		"Never let your emotions overpower your intelligence.",
		"I don’t need it to be easy, I need it to be worth it.",
		"Oh, the things you can find, if you don’t stay behind.",
		"Have enough courage to start and enough heart to finish.",
		"Nothing lasts forever but at least we got these memories.",
		"If you tell the truth you don’t have to remember anything.",
		"Hate comes from intimidation, love comes from appreciation.",
		"If you tell the truth, you don't have to remember anything.",
		"Dream as if you’ll live forever, live as if you’ll die today.",
		"If I’m gonna tell a real story, I’m gonna start with my name.",
		"Cowards die many times before their deaths; the valiant never taste of death but once.",
		"One day the people that don’t even believe in you will tell everyone how they met you.",
		"The very word “secrecy” is repugnant in a free and open society; and we are as a people inherently and historically opposed to secret societies, to secret oaths and to secret proceedings. We decided long ago that the dangers of excessive and unwarranted concealment of pertinent facts far outweighed the dangers which are cited to justify it. John F Kennedy"

	]

numPass = sum(text.lower() == caesar.salad(text) for text in quotes)
print(numPass, '/', len(quotes), 'tests passed')
print(str(float(numPass * 100)/len(quotes)) + '%')