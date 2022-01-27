import discord
import requests
import time
import json
from bs4 import BeautifulSoup

client = discord.Client()


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("$info"):
      embed = discord.Embed(title="JumpTask information", description="[Website](https://www.jumptask.io/) - [Whitepaper](https://gitbook.jumptask.io/) - [Token](https://bscscan.com/token/0x88d7e9b65dc24cf54f5edef929225fc3e1580c25)")
      embed.add_field(name="User side", value="JumpTask will offer its users a chance to earn money by completing simple microtasks that will not require specific knowledge, experience, or serious time investment. The tasks will be categorized according to their nature and complexity and introduced gradually from the simplest to more challenging in terms of their development and verification.")
      embed.add_field(name="Partner side", value="JumpTask's partners will have to define certain parameters of the task they need completed, including but not limited to the type of task, rules of completion validation, duration of the campaign, and reward size in JMPT. To be able to issue the rewards, they will also have to top up their JumpTask balance with JumpTokens (JMPT) prior to activating the campaigns.")
      embed.add_field(name="From platform to protocol", value="JumpTask will act as an interim platform to onboard existing businesses and to create task protocols that use JumpToken. All the active task modules that prove to work successfully will be used to create templates for future smart contracts. These can then be validated directly on the blockchain with no intermediaries and allow for easier and more convenient use.")
      embed.set_image(url="https://static.wixstatic.com/media/a3f5b0_12f075ae75c147f49cfb5f58832f0752~mv2.png/v1/fill/w_920,h_497,al_c,q_90,usm_0.66_1.00_0.01/JT%20Scheme%203%20_%201%20_%20Dark.webp")
      await message.channel.send(embed=embed)

  if message.content.startswith("$roadmap"):
      embed = discord.Embed(title="JumpTask Roadmap")
      embed.add_field(name="2022 Q1", value="-JumpTask Platform\n-JumpToken Release\n-Initial Module\n-100K Users\n-DEX offering")
      embed.add_field(name="2022 Q2", value="-JumpTask Android App\n-Survey Module\n-1M Users")
      embed.add_field(name="2022 Q3/4", value="-JumpTask iOS APP\n-AppReview Module\n-1 Billion Tasks\n-5M Users")
      embed.add_field(name="2023", value="-Attention Task Module\n-Action Task Module\n-10 Billion Tasks\n-20M Users")
      embed.add_field(name="2024", value="-Data Task Module\n-50 Billion Tasks\n-50M Users")
      await message.channel.send(embed=embed)

  if message.content.startswith('$jmpt'):
      price = requests.get("https://api.jumptask.io/currency/").json()["data"]["usd"]
      price = price.split(".")
      headers = {
          "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
      }
      holders = requests.get("https://bscscan.com/token/0x88d7e9b65dc24cf54f5edef929225fc3e1580c25", headers=headers)
      soup = BeautifulSoup(holders.content, 'html.parser')
      page = soup.find("div", {"class":'mr-3'}).getText()
      page = page.split("a")[0]
      embed = discord.Embed(title="JumpToken Stats")
      embed.add_field(name="Price", value="$" + price[0] + "." + price[1][:3])
      embed.add_field(name="Holders", value=page.strip())
      await message.channel.send(embed=embed)
  
    
client.run("")
    