## Methodology

| Column | Full Name | Reasoning | Used |
|---|---|---|---|
| PTS | Points | Points is a collection of wins/losses and overtime/shootout wins/losses; it will be the representation of these statistics. | ✅ |
| PTS% | Points Percentage | Points percentage provides more detail to PTS, it allows us to see the nuance of overtime/shootout wins/losses as a percentage. | ✅ |
| GF | Goals For | Linearly demonstrates the team's attacking ability. | ✅ |
| GA | Goals Against | Linearly demonstrates the team's defensive ability. | ✅ |
| SRS | Simple Rating System | The Simple Rating System describes a team's ability against hard and easy opponents. It shows us their skill level outside of wins and losses. | ✅ |
| GF/G | Goals For Per Game | Goals For Per Game gives us the average of our GF stat. | ✅ |
| GA/G | Goals Against Per Game | Goals Against Per Game gives us the average of our GA stat. | ✅ |
| PP% | Power Play Percentage | Demonstrates how well teams utilize advantages. | ✅ |
| PPA | Power Play Goals Against | Demonstrates how often teams falter with advantages. | ✅ |
| PK% | Penalty Kill Percentage | Demonstrates how well teams shut down opponents' advantages. | ✅ |
| SH | Short Handed Goals For | Demonstrates how well teams steal opponents' advantages. | ✅ |
| AvAge | Average Age | How does a team's age affect its winning potential? Do Cup winners skew older or younger, and has that changed over time? | ✅ |
| S | Shots For | How often teams are able to shoot on the net seems pertinent to their overall pressure. | ✅ |
| S% | Shooting Percentage | How often teams are able to score from their shots demonstrates "Good" shot selection. | ✅ |
| SA | Shots Against | How often teams give up pressure is important to detecting their defensive abilities. | ✅ |
| SV% | Save Percentage | A goalie's ability to stop shots will help us navigate the totality of the defence. | ✅ |
| PPOA | Power Play Opportunities Against | Demonstrates how often teams almost falter with advantages. It could be a useful stat to show how "Lucky" teams get. | ❌ |
| PIM/G | Penalty Minutes Per Game | This shows us how often teams take penalties, but nothing else. More useful information is described in the PK%, PP%, and PPA. | ❌ |
| oPIM/G | Opponent Penalty Minutes Per Game | Same reasoning as above. However, this could give us an idea of how well teams draw advantages, but it wouldn't be possible to determine if these were offsetting penalties or not, given the dataset. | ❌ |
| Rk | Rank | A team's rank is an aggregate of all of its stats. Its value is simply to centralize all other stats. | ❌ |
| Team | Team Name | The name of the team does not affect its winning potential… I think. | ❌ |
| GP | Games Played | Games played vary across seasons. To prevent this from skewing results, it is left out. | ❌ |
| W | Wins | Wins may be useful in this analysis; however, I am currently unsure if they are simply reflected in other stats or would make the prediction linear: "Teams that win more, win more." | ❌ |
| L | Losses | Losses have the same reasoning as the above statement. | ❌ |
| OL | Overtime Losses | Overtime losses have the same reasoning as the above statements; however, they may be more useful as they demonstrate close losses. | ❌ |
| SOW | Shootout Wins | Shootout wins are demonstrated in PTS% and PTS. | ❌ |
| SOL | Shootout Losses | Shootout losses are demonstrated in PTS% and PTS. | ❌ |
| SOS | Strength of Schedule | Strength of Schedule is demonstrated in the Simple Rating System as a byproduct. This stat also only ranges from 0.06 to -0.07 in my initial analysis of this dataset. | ❌ |
| PP | Power Play Goals | Power Play Goals are demonstrated in a later stat. | ❌ |
| PPO | Power Play Opportunities | Power Play Opportunities are demonstrated in a later stat. | ❌ |
| SHA | Short Handed Goals Against | Short-handed goals against is demonstrated in a team's PK%. | ❌ |
| SO | Shutouts | Shutouts are simply a collection of the above defensive stats; they don't add any more value in my opinion. | ❌ |


## Data reference
https://www.hockey-reference.com 
