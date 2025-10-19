# TCG Pack Generator

## General Information

This generator simulates opening packs and thus will not directly reflect the real thing. E.g. Machamp (PokemonTCG Base 8) is normaly unobtainable via a booster pack but is in this generator.

### Pool Names

| PoolName | Cards |
| --- | --- |
| `Common` | Common cards |
| `Uncommon` | Uncommon cards |

## JSON Formats

### TCG

The `TCG.json` file requres sets to be defined as such
```json
"": { // Name of the set
	"PackCards": [], // The number of "slots" of each rarity in the format "<rarity> <numberOfSlots>"
	"Ratios": [], // The chance of a slot getting a differnt pool of cards e.g. rares becoming holo rares in the format "<raritySlot> <chance> <newPool>"
	"Pools": { // The cards in each pool by set number
		"Common": [],
		"Uncommon": [],
		"Rare": [],
		<ect.>
	}
}
```

## Sources

Pull rates and card order - https://github.com/Pepper0ni/TTS-PTCG-Pack-Simulator/wiki/Pull-rate-and-card-order-Information  
Set lists - https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_Trading_Card_Game_expansions
