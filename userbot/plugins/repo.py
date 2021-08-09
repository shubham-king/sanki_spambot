@bot.on(admin_cmd(pattern="repo"))
@bot.on(sudo_cmd(pattern="repo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    Repo = f"[Click Here](https://github.com/YukkiBot/YukkiSpamBot)"
    Deploy = f"[Click Here](https://t.me/RobotTech_official)"
    await edit_or_reply(
        event, f"**SANKI  Spam Bot Repo:** {Repo}\n\n**Channel:** {Deploy}"
    )
