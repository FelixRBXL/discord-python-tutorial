## Füge den Code ganz einfach in deine 'bot.py' ein.

#-- Userinfo --#
@client.command(name="userinfo")
async def userinfo(ctx, member:discord.Member=None):
    if member == None:
        member = ctx.author
    embed=discord.Embed(description=member.mention, color=0xff0000)
    embed.add_field(name="Server beigetreten", value=member.joined_at)
    embed.add_field(name="Discord beigetreten", value=member.created_at)
    if len(member.roles) > 1:
        role_string = ' '.join([r.mention for r in member.roles][1:])
        embed.add_field(name="Rollen [{}]".format(len(member.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
    embed.add_field(name="Server Berechtigungen", value=perm_string, inline=False)
    embed.set_author(name=f"{ctx.author.name}", icon_url=str(ctx.author.avatar_url))
    embed.set_footer(text=f"ID: {member.id}")
    await ctx.send(embed=embed)
    
    #-- Serverinfo --#
@client.command(name="serverinfo")
async def serverinfo(ctx):
    embed=discord.Embed(color=0xff0000)
    embed.set_author(name=f"{ctx.guild.name}", icon_url=str(ctx.guild.icon_url))
    embed.add_field(name="Owner", value=str(ctx.guild.owner))
    embed.add_field(name="Sprach-Kanäle", value=len(ctx.guild.categories))
    embed.add_field(name="Text-Kanäle", value=len(ctx.guild.text_channels))
    embed.add_field(name="Sprach-Kanäle", value=len(ctx.guild.voice_channels))
    embed.add_field(name="Mitglieder", value=ctx.guild.member_count)
    embed.add_field(name="Rollen", value=len(ctx.guild.roles))
    embed.set_thumbnail(url=str(ctx.guild.icon_url))
    embed.set_footer(text=f"ID: {ctx.guild.id}")
    await ctx.send(embed=embed)
