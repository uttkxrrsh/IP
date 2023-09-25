# INFLATION DICTIONARY
from nltk.stem import PorterStemmer

ConsumerPricesInflation_Hawkish = ["accelerated", "boosted", "elevated", "escalated", "high", "hightened", "increased", "jumped", "pickup", "risen", "rising", "rose", "runup", "run-up", "strongness", "surged", "upped"]
ConsumerPricesInflation_Dovish = ["decelarated", "declined", "decreased", "downed", "dropped", "fallen", "falling", "fell", "lowest", "lowed", "lowered", "muted", "reduced", "slowed", "stable", "subdued", "weak", "weakened", "contained"]

InflationPressure_Hawkish = ["accelerated", "boosted", "building", "elevated", "emerged", "great", "greatening", "heighten", "highed", "increased", "intensified", "mounted", "mountained", "pickup", "rise", "rose","rising","stoked", "stokened", "sustained"]
InflationPressure_Dovish = ["abated", "contained", "dampened", "decelerated", "declined", "decreased", "diminish", "eased", "easy", "falling", "fallen", "fell", "lowest", "lowed", "lowered", "moderated", "receded", "reduced", "subdued", "tempered"]

InterestRate_Hawkish = ["accelerated", "boosted", "elevated", "escalated", "high", "hightened", "increased", "jumped", "pickup", "rised", "rising", "rose", "runup", "run-up", "strongness", "surged", "upped", "increase"]
InterestRate_Dovish = ["decelarated", "declined", "decreased", "downed", "dropped", "fallen", "falling", "fell", "lowest", "lowed", "lowered", "muted", "reduced", "slowed", "stable", "subdued", "weak", "weakened", "contained", "decrease"]

# ECONOMIC ACTIVITY DICTIONARY
# edged up, picked up
ConsumerSpending_Hawkish = ["accelerated", "edged up", "expanded", "increased", "picked up", "pickup", "softened", "strengthened", "strongness", "weak", "weakened"]
ConsumerSpending_Dovish = ["contracted", "decelerated", "decreased", "dropped", "retrenched", "slowed", "slugged", "softened", "subdued"]

# edged up, picked up, stepped up
EconomicActivity_Hawkish = ["accelerated", "buoyant", "edged up", "expanded", "increased", "high", "hightened", "picked up", "pickup", "risen", "rose", "rising", "stepped up", "strenghthened", "strongness", "upside"]
EconomicActivity_Dovish = ["contracted", "curtailed", "decelerated", "declined", "decreased", "downside", "drop", "fallen", "falling", "fell", "lowest", "lowed", "lowered", "moderated", "slowed", "slugged","weak", "weakened"]

ResourceUtilization_Hawkish = ["high", "hightened", "increased", "rise", "rising", "rose", "tight", "tightened"]
ResourceUtilization_Dovish = ["declined", "fallen", "falling", "fell", "loosened", "lowed", "lowered", "lowest"]


# EMPLOYMENT DICTIONARY
# picked up, turned up
Employment_Hawkish = ["expanded", "gained", "improved", "increased", "picked up", "pickup", "raised", "risen" "rising", "rose", "strengthened", "turned up"]
Employment_Dovish = ["slowed", "declined", "reduced", "weak", "weakened", "deteriorated", "shrink", "shrinking", "shrank", "falling", "fallen", "fell", "drop", "contracted", "sluggish"]

LaborMarket_Hawkish = ["strained", "tightened"]
LaborMarket_Dovish = ["eased", "easing", "loosened", "loosening", "softened", "softening", "weakened", "weakening"]

Unemployment_Hawkish = ["declined", "declining", "fallen", "falling", "fell", "lowest", "lowed", "lowered", "reduced"]
Unemployment_Dovish = ["increased", "increasing", "rose", "rising", "risen", "high", "elevated"]


# stem each list made in above cell
stemmer = PorterStemmer()
ConsumerPricesInflation_Hawkish = [stemmer.stem(word) for word in ConsumerPricesInflation_Hawkish]
# print(ConsumerPricesInflation_Hawkish)
ConsumerPricesInflation_Dovish = [stemmer.stem(word) for word in ConsumerPricesInflation_Dovish]
# print(ConsumerPricesInflation_Dovish)
InflationPressure_Hawkish = [stemmer.stem(word) for word in InflationPressure_Hawkish]
# print(InflationPressure_Hawkish)
InflationPressure_Dovish = [stemmer.stem(word) for word in InflationPressure_Dovish]
# print(InflationPressure_Dovish)
ConsumerSpending_Hawkish = [stemmer.stem(word) for word in ConsumerSpending_Hawkish]
# print(ConsumerSpending_Hawkish)
ConsumerSpending_Dovish = [stemmer.stem(word) for word in ConsumerSpending_Dovish]
# print(ConsumerSpending_Dovish)
EconomicActivity_Hawkish = [stemmer.stem(word) for word in EconomicActivity_Hawkish]
# print(EconomicActivity_Hawkish)
EconomicActivity_Dovish = [stemmer.stem(word) for word in EconomicActivity_Dovish]
# print(EconomicActivity_Dovish)
ResourceUtilization_Hawkish = [stemmer.stem(word) for word in ResourceUtilization_Hawkish]
# print(ResourceUtilization_Hawkish)
ResourceUtilization_Dovish = [stemmer.stem(word) for word in ResourceUtilization_Dovish]
# print(ResourceUtilization_Dovish)
Employment_Hawkish = [stemmer.stem(word) for word in Employment_Hawkish]
# print(Employment_Hawkish)
Employment_Dovish = [stemmer.stem(word) for word in Employment_Dovish]
# print(Employment_Dovish)
LaborMarket_Hawkish = [stemmer.stem(word) for word in LaborMarket_Hawkish]
# print(LaborMarket_Hawkish)
LaborMarket_Dovish = [stemmer.stem(word) for word in LaborMarket_Dovish]
# print(LaborMarket_Dovish)
Unemployment_Hawkish = [stemmer.stem(word) for word in Unemployment_Hawkish]
# print(Unemployment_Hawkish)
Unemployment_Dovish = [stemmer.stem(word) for word in Unemployment_Dovish]
# print(Unemployment_Dovish)
