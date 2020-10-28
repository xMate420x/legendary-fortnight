import random;

def rng(sentencenum):
    prefixes = ["refactored","reimagined","stunning","sturdy","solid","cuddly","literate","animated","silver","psychic","congenital","crispy","special","legendary","expert"]
    suffixes = ["pancake","guide","succotash","lamp","happiness","machine","carnival","umbrella","system","waddle","potato","tree","parakeet","guacamole","eureka","fortnight"]
    infixes = ["octo", "computing", "palm"]

    if(sentencenum == 3): print(random.choice(prefixes)+"-"+random.choice(infixes)+"-"+random.choice(suffixes))
    else: print(random.choice(prefixes)+"-"+random.choice(suffixes))

if(random.randint(0, 10) == 10): rng(3);
else: rng(2);
