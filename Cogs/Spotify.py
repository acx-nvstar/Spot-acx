import discord
import time
from discord.ext import commands


class Spotify(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def music(self, ctx, *, music = None):
        sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = "690da446e39b44a7baf8deaff12be418",
                                                                     client_secret = "782ddebbf58846f1a1d70a074d62ce1a"))

        results = sp.search(q = f'{music}', limit = 1)
        for idx, track in enumerate(results['tracks']['items']):
            artist_name = track['artists'][0]['name']
            album_info = track['album']
            album_images = album_info['images'][0]
            album_images_url = album_images['url']
            album_artist = album_info['artists'][0]
            album_artist_name = album_artist['name']
            external_urls = track['external_urls']
            #external_urls_json = json.loads(external_urls)
            track_name = track['name']
            spotify_urls = external_urls['spotify']
            #embed dan hasil output
            em = discord.Embed(title = None, 
                               color = 0XFF8C00, 
                               description = f"> [{album_artist_name} - {track_name}]({spotify_urls})\n> \n> • [DISCLAIMER](https://github.com/acinonyx-esports/Acinonyx-Bot/wiki/SPOTIFY-DOWNLOADER-DISCLAIMER)\n> • [HOW THIS BOT IS WORK?](https://github.com/acinonyx-esports/Acinonyx-Bot/wiki/HOW-SPOTIFY-DOWNLOADER-IS-WORK%3F)\n> \n> <a:acx_mp3:744868331382767617> **.MP3 Format**")
            em.set_author(name = "Spotify downloader", 
                          url = "https://github.com/acinonyx-esports/Acinonyx-Bot/wiki/SPOTIFY-DOWNLOADER-DISCLAIMER", 
                          icon_url = "https://cdn.discordapp.com/attachments/726031951101689897/739778620658155602/spotify-logo-png-7061.png")
            em.set_thumbnail(url = album_images_url)
            em.set_footer(text = "Request by : {}".format(ctx.message.author.name),
                          icon_url = ctx.message.author.avatar_url)
            msg = await ctx.send(embed = em, delete_after = 15)
            await msg.add_reaction('<a:acx_mp3:744868331382767617>')
            while True:
                    reaction, user = await self.client.wait_for(event='reaction_add',)
                    if user == ctx.author:
                        emoji = str(reaction.emoji)
                        if emoji == '<a:acx_mp3:744868331382767617>':
                            await msg.delete()
                            s = Savify(api_credentials=("690da446e39b44a7baf8deaff12be418","782ddebbf58846f1a1d70a074d62ce1a"),
                                       quality = Quality.BEST,
                                       download_format = Format.MP3,
                                       group='{}'.format(ctx.author.id),
                                       output_path=Path('/home/nvstar/Corp-ina.py/Temp'))
                            em = discord.Embed(title = None, 
                                               color = 0XFF8C00, 
                                               description = f"[{album_artist_name} - {track_name}]({spotify_urls})\n" + processing_file)
                            em.set_author(name = "Spotify downloader",
                                          url = "https://github.com/acinonyx-esports/Acinonyx-Bot/wiki/SPOTIFY-DOWNLOADER-DISCLAIMER",
                                          icon_url = "https://cdn.discordapp.com/attachments/726031951101689897/739778620658155602/spotify-logo-png-7061.png")
                            em.set_thumbnail(url = album_images_url)
                            em.set_footer(text = f"{ctx.author}",
                                          icon_url = ctx.message.author.avatar_url)
                            dld = await ctx.send(embed = em)

                            musicDownload = s.download("{}".format(spotify_urls))

                            checkServer = ctx.guild.premium_tier
                            if checkServer > 1:
                                em = discord.Embed(title = None, 
                                                    color = 0XFF8C00 , 
                                                    description = f"[{album_artist_name} - {track_name}]({spotify_urls})\n" + uploading_file)
                                em.set_author(name = "Spotify downloader",
                                              url = "https://github.com/acinonyx-esports/Acinonyx-Bot/wiki/SPOTIFY-DOWNLOADER-DISCLAIMER",
                                              icon_url = "https://cdn.discordapp.com/attachments/726031951101689897/739778620658155602/spotify-logo-png-7061.png")
                                em.set_thumbnail(url = album_images_url)
                                em.set_footer(text = f"{ctx.author}",
                                               icon_url = ctx.message.author.avatar_url)
                                await dld.edit(embed = em)
                                await ctx.send(file = discord.File(f"/home/nvstar/Corp-ina.py/Temp/{ctx.author.id}/{artist_name} - {track_name}.mp3"))

                                botKernel_DeleteFile = subprocess.Popen(["rm", "-rf", f"/home/nvstar/Corp-ina.py/Temp/{ctx.author.id}/{artist_name} - {track_name}.mp3"], stdout = subprocess.PIPE).communicate()[0]
                                
                                await dld.delete()
                                await ctx.send(f"{ctx.author.mention} :arrow_up:")

                            checkFile = os.path.getsize(f"/home/nvstar/Corp-ina.py/Temp/{ctx.author.id}/{artist_name} - {track_name}.mp3")
                            if checkFile > 8000000:
                                await dld.delete()
                                em = discord.Embed(
                                    title = "<a:exclamation:750557709107068939>**EXCEED THE LIMIT**<a:exclamation:750557709107068939>",
                                    color = 0XFF8C00,
                                    description = f"[{album_artist_name} - {track_name}]({spotify_urls})\n\n" + upload_dropbox)
                                em.set_thumbnail(url = album_images_url)
                                em.set_footer(text = f"{ctx.author}", 
                                              icon_url = f"{ctx.author.avatar_url}")
                                msg2 = await ctx.send(embed = em)

                                # MEMULAI UPLOAD DROPBOX
                                dropbox_access_token = "INmLpmjvCLQAAAAAAAAAAa--h2Jb571-pTJ_UHPdqp3XoMC0KJuSekPufnCI-a2y"
                                computer_path = '/home/nvstar/Corp-ina.py/Temp/{}/{} - {}.mp3'.format(ctx.author.id, artist_name, track_name)
                                dropbox_path = f"/Apps/Acinonyc music file/{album_artist_name} - {track_name}.mp3"
                                client = dropbox.Dropbox(dropbox_access_token)
                                print("[SUCCESS] dropbox account linked")
                                client.files_upload(open(computer_path, "rb").read(), dropbox_path, mode = dropbox.files.WriteMode("overwrite"))
                                print("[UPLOADED] {}".format(computer_path))
                                d = dropbox.Dropbox(dropbox_access_token)
                                target = dropbox_path
                                link_dropbox = d.sharing_create_shared_link(target)
                                dl_link = re.sub(r"\?dl\=0", "?dl=1", str(link_dropbox.url))
                                botKernel_DeleteFile = subprocess.Popen(["rm", "-rf", '/home/nvstar/Corp-ina.py/Temp/{}/{} - {}.mp3'.format(ctx.author.id, artist_name, track_name)], stdout = subprocess.PIPE).communicate()[0]
                                
                                #EMBED FILE SELESAI UPLOAD
                                em = discord.Embed(
                                    title = None,
                                    color = 0XFF8C00,
                                    description = f"{upload_complete}\n**[DOWNLOAD HERE]({dl_link})**")
                                em.set_author(name = "Spotify downloader",
                                               url = "https://github.com/acinonyx-esports/Acinonyx-Bot/wiki/SPOTIFY-DOWNLOADER-DISCLAIMER",
                                               icon_url = "https://cdn.discordapp.com/attachments/726031951101689897/739778620658155602/spotify-logo-png-7061.png")
                                em.set_thumbnail(url = album_images_url)
                                em.set_footer(text = f"{ctx.author.name}", icon_url = f"{ctx.author.avatar_url}")
                                await msg2.delete()
                                msg3 = await ctx.send(embed = em)

                                #DELETE FILES
                                await asyncio.sleep(420)
                                dropbox_delete = d.files_delete(dropbox_path)
                                await msg3.delete()                             

                            em2 = discord.Embed(title = None, 
                                                color = 0XFF8C00 , 
                                                description = f"[{album_artist_name} - {track_name}]({spotify_urls})\n" + uploading_file)
                            em2.set_author(name = "Spotify downloader",
                                          url = "https://github.com/acinonyx-esports/Acinonyx-Bot/wiki/SPOTIFY-DOWNLOADER-DISCLAIMER",
                                          icon_url = "https://cdn.discordapp.com/attachments/726031951101689897/739778620658155602/spotify-logo-png-7061.png")
                            em2.set_thumbnail(url = album_images_url)
                            em2.set_footer(text = f"{ctx.author}",
                                           icon_url = ctx.message.author.avatar_url)
                            await dld.edit(embed = em2)
                            await ctx.send(file = discord.File('/home/nvstar/Corp-ina.py/Temp/{}/{} - {}.mp3'.format(ctx.author.id, artist_name, track_name)))

                            botKernel_DeleteFile = subprocess.Popen(["rm", "-rf", '/home/nvstar/Corp-ina.py/Temp/{}/{} - {}.mp3'.format(ctx.author.id, artist_name, track_name)], stdout = subprocess.PIPE).communicate()[0]
                            
                            await dld.delete()
                            await ctx.send(f"{ctx.author.mention} :arrow_up:")
                    # if self.bot.user != user:
                    #     await msg.remove_reaction()

def setup(client):
    client.add_cog(Spotify(client))
