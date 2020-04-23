"""
to do system, work, crime, jackpot, tax, steal, tansfer, time lock, 
"""
import discord
from discord.ext import commands
import json
import random
money = {}
class eco:
    def __init__(self, Bot):
        self.Bot = Bot

    async def on_ready(self):
        global money
        try:
            with open('money.json') as f:             
                money = json.load(f)
        except FileNotFoundError:
            print('could not load money.json')
            money = {}

    @commands.command(pass_context=True)
    async def my_stats(self,ctx):
        id = ctx.message.author.name
        hp = money['users'][id]['stats']['hp']
        atk = money['users'][id]['stats']['atk']
        pro = money['users'][id]['stats']['protect']
        await self.Bot.say('you HP is {} your atk is {} your protection is {}'.format(hp,atk,pro))
        

    @commands.command(pass_context=True)
    async def testcom(self,ctx):
        me = '513936641199570975'
        if ctx.message.author.id == me:

            look = money['users']
            t = 0
            ta = 0
            ignore = ('TAX')
            get_mon = money['users']['TAX']['cash']
            users = []
            for i in look:
                if i == ignore:
                    print('ignoring',i)
                else:        
                    print(i)
                    users.append(i)
                    t += 1
            div = get_mon // t
            for i in users:
                money['users'][i]['cash'] += int(div)
                await self.Bot.say('{} has gained {} '.format(i,div))
            money['users']['TAX']['cash'] -= get_mon
            await self.save()
            print(t)
        else:
            await self.Bot.say('fuck off')



    @commands.command(pass_context=True)
    async def donate(self,ctx,amount:int=None):
        id = ctx.message.author.name
        if amount <0:
            await self.Bot.say('nope')
        if not amount:
            await self.Bot.say('how much do u want to donate')
            return
        money['users'][id]['cash'] -= amount
        money['users']['TAX']['cash'] += amount
        await self.save()
        tx = money['users']['TAX']['cash']
        await self.Bot.say('the tax system gained {} and now has {}'.format(amount,tx))

    @commands.command(pass_context=True)
    async def train(self,ctx,stat=None,gain:int=None):
        id = ctx.message.author.name
       # ty = money['users'][id]['stats'][stat]
        if not stat:
            await self.Bot.say('what stat')
        if not gain:
            await self.Bot.say('how much lvls u want to gain 1 lvl = 10k')
        try:
            #ty = money['users'][id]['stats'][stat]
            if stat == 'protect':
                await self.train_pro(id,stat,int(gain))
            else:
                await self.training(id,stat,int(gain))
            #print('hi')

        except Exception as error:
            await self.Bot.say('supported stats atk,hp,protect not {}'.format(error))

    async def train_pro(self,id,stat,gain:int):
        spend = gain * 10000
        plus = gain / 100
        #print(plus)
        if spend <= 0:
            await self.Bot.say('no - ')
        if money['users'][id]['cash'] < spend:
            await self.Bot.say('you cant afford that')
        else:
            money['users'][id]['stats'][stat] += plus
            money['users'][id]['cash'] -= spend
            await self.save()
            
    async def training(self,id,stat,gain:int):
        spend = gain * 10000
        if spend <= 0:
            await self.Bot.say('no - ')
        if money['users'][id]['cash'] < spend:
            await self.Bot.say('you cant afford that')
        else:
            money['users'][id]['stats'][stat] += gain
            money['users'][id]['cash'] -= spend
            await self.save()

    @commands.command(pass_context=True)
    async def fight(self,ctx):
        id = ctx.message.author.name
        #deff = member.name
        ai = 'slime'
        await self.statget(id,ai)

    async def statget(self,id,ai):
        atk = money['users'][id]['stats']['atk']
        hp = money['BOTS'][ai]['stats']['hp']
        pro = money['BOTS'][ai]['stats']['protect']
        cash = money['BOTS'][ai]['cash']
        await self.fightsys(id,ai,atk,hp,pro,cash)

    async def fightsys(self,id,ai,atk,hp,pro,cash):
        r1 = hp - atk
        r2 = r1 - atk
        r3 = r2 - atk
        r4 = r3 - atk
        last = r4 - atk
        if r1 <= 0:
            await self.Bot.say( 'you won {} '.format(id))
            await self.profiet(id,ai,atk,pro,cash)
            return
        if r2 <= 0:
            await self.Bot.say(' you won {} '.format(id))
            await self.profiet(id,ai,atk,pro,cash)
            return
        if r3 <= 0:
            await self.Bot.say(' you won {} '.format(id))
            await self.profiet(id,ai,atk,pro,cash)
            return
        if r4 <= 0:
            await self.Bot.say(' you won {} '.format(id))
            await self.profiet(id,ai,atk,pro,cash)
            return
        if last <= 0:
            await self.Bot.say(' you won {} '.format(id))
            await self.profiet(id,ai,atk,pro,cash)
            return
        else:
            await self.Bot.say('{} won and {} lost : hp left {} '.format(ai,id,last))

    async def profiet(self,id,ai,atk,pro,cash):
        if atk < cash:
            pos_gain = atk
            earn = int(pos_gain * pro)
            gained = int(pos_gain - earn)
            await self.Bot.say(pos_gain)
            await self.Bot.say(earn)
            await self.Bot.say(gained)
            money['users'][id]['cash'] += gained
        else:
            pos_gain = cash
            earn = pro * pos_gain
            gained = pos_gain - earn
            await self.Bot.say(pos_gain)
            await self.Bot.say(earn)
            await self.Bot.say(gained)
            money['users'][id]['cash'] += gained
        await self.save()

    
    @commands.command(pass_context=True)
    async def shop(self,ctx,items=None):
        id = ctx.message.author.name
        amon = 10000000000
        hve = money['users'][id]['cash']
        if not items:
            await self.Bot.say('what do you want to buy?')
            await self.Bot.say('Admin, more comming soon if i think hard enough')
        if items == 'Admin':
            await self.Bot.say('1 moment pls')
            if hve >= amon:
                await self.Bot.say('sometime tonite or tmr i will add it')
            else:
                await self.Bot.say('not enough KKC')

            
    @commands.command(pass_context=True)
    async def transfer(self,ctx,amount:int=None,member: discord.Member=None):
        id = ctx.message.author.name
        person = member.name
        if amount <= 0:
            await self.Bot.say('dont try to cheat me cunt')
            return
        if not amount:
            await self.Bot.say('specify an amount')
            return
        if not member:
            await self.Bot.say('pls specify a user')
            return
        if id not in money['users']:
            await self.Bot.say('you are not in the money sys')
            return
        if person not in money["users"]:
            await self.Bot.say('user is not registerd')
            return
        if amount <= money['users'][id]['cash']:
            await self.Bot.say('ok then')
            await self.trans(id,amount,person)

        else: 
            await self.Bot.say("You dont have that much money")

    @commands.command(pass_context=True)
    async def other_stats(self,ctx,member: discord.Member=None):
        person = member.name
        me = money["users"][person]['cash']
        await self.Bot.say('{} has {} KKC'.format(person,me))

    @commands.command(pass_context=True)
    async def stats(self,ctx):
        id = ctx.message.author.name
        me = money["users"][id]['cash']
        await self.Bot.say('you have {} KKC'.format(me))

    
    @commands.command(pass_context=True)
    async def gamble(self,ctx,amount:int=None):
        id = ctx.message.author.name
        KKC = money["users"][id]['cash']
        if not amount:
            await self.Bot.say('you forgot the amount you want to gamble || ~gamble x')
        else:
            if id not in money["users"]:
                await self.Bot.say('you dont have an account try again now')
            else:
                if amount <= 0:
                    await self.Bot.say('dont try to cheat me cunt')
                else:
                    if KKC >= amount:
                        await self.roll(id,amount)
                    else:
                        await self.Bot.say('you have {} KKC and you wanted to gamble {} KKC HA gl'.format(KKC,amount))


    @commands.command(pass_context=True)
    async def make(self,ctx,am:int=None):
        id = ctx.message.author.name
        admon = '513936641199570975'
        if not am:
            if id not in money["users"]:
                await self.Bot.say('you are not in the json i will add you')
                money["users"][id] = {}
                money["users"][id]["cash"] = 0
                money["users"][id]["stats"] = {}
                money["users"][id]["stats"]['hp'] = 100
                money["users"][id]["stats"]['atk'] = 10
                money["users"][id]["stats"]['protect'] = float(0.01)
                await self.save()
            else:
                await self.Bot.say('{} ok'.format(id))
                await self.make_the_money(id)
        else:
            if ctx.message.author.id == admon:
                await self.Bot.say('{} ok'.format(id))
                await self.make_the_money(id,am)
            else:
                await self.Bot.say('that is a debug option for spanky only')

    @commands.command(pass_context=True)
    async def tax(self,ctx):
        tx = money['users']['TAX']['cash']
        await self.Bot.say('the tax sys has made about {} KKC '.format(tx))

    @commands.command(pass_context=True)
    async def admin_gamble(self,ctx,amount:int=None,WOL=None):
        id = ctx.message.author.name
        me = '513936641199570975'
        auth = ctx.message.author.id
        if not amount:
            await self.Bot.say('how much do u want to gamble')
            return
        if not WOL:
            await self.Bot.say('which type')
            return
        if auth == me:
            if WOL == 'true':
                await self.dwin(id,amount)
                await self.Bot.say('x3 win')
            else:
                await self.won(id,amount)
                await self.Bot.say(' win')
        else:
            await self.Bot.say('fuck off spankys command only')
    async def trans(self,id,amm,user):
        money['users'][id]['cash'] -= amm
        money['users'][user]['cash'] += amm
        await self.save()
        

    
    async def roll(self,id,amm):
        dev = 'false'
        if dev == 'true':
            await self.dwin(id,amm)
            await self.Bot.say('dev mode')
            return
        num = [1,2,3,4,5,6,7,8,9,10,11,12]
        Win = [9,10,11,12]
        loss = [1,2,3,4,5,6,7,8]
        roll = random.choice(num)
        r2 = random.choice(Win)
        #await self.Bot.say('num {}, win {}, loss {}, roll {}, r2 {} '.format(num,Win,loss,roll,r2))
        if roll in loss:
            await self.Bot.say('better luck next time')
            await self.lose_the_money(id,amm)
        else:
            if roll == r2:
                await self.Bot.say('you won 3x')
                await self.dwin(id,amm)
            else:
                await self.Bot.say('u won')
                await self.won(id,amm)

    async def won(self,id,amm):
        x = amm 
        z = x * .75
        x_z = x - z
        #await self.Bot.say(x)
        #await self.Bot.say(z)
        #await self.Bot.say(x_z)
        money['users'][id]['cash'] += int(z)
        money['users']['TAX']['cash'] += int(x_z)
        await self.Bot.say('you now have {} KKC'.format(money['users'][id]['cash']))
        await self.save()

    async def dwin(self,id,amm):
        x = amm * 3
        #dtotal = total * 2
        money['users'][id]['cash'] += x
        await self.Bot.say('you now have {} KKC'.format(money['users'][id]['cash']))
        await self.save()

    async def lose_the_money(self,id,amm):
        lose = amm
        money["users"][id]["cash"] -= lose
        money["users"]['TAX']["cash"] += lose
        await self.Bot.say('you now have {} KKC'.format(money['users'][id]['cash']))
        await self.save()

    async def make_the_money(self,id,am:int=None):
        if not am:
            money["users"][id]["cash"] += 100
            await self.save()
        else:
            money["users"][id]["cash"] += am
            await self.save()

    async def save(self):
        with open('money.json', 'w+') as f:
            json.dump(money, f,indent=4)

def setup(Bot):
    Bot.add_cog(eco(Bot))