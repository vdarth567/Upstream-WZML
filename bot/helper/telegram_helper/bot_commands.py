#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'pmirror{CMD_SUFFIX}', f'pm{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'pqbmirror{CMD_SUFFIX}', f'pqm{CMD_SUFFIX}']
        self.YtdlCommand = [f'pytdl{CMD_SUFFIX}', f'py{CMD_SUFFIX}']
        self.LeechCommand = [f'pleech{CMD_SUFFIX}', f'pl{CMD_SUFFIX}']
        self.QbLeechCommand = [f'pqbleech{CMD_SUFFIX}', f'pql{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'pytdlleech{CMD_SUFFIX}', f'pyl{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'punzipmirror{CMD_SUFFIX}', f'puzm{CMD_SUFFIX}', f'pzipmirror{CMD_SUFFIX}', f'pzm{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'pqbunzipmirror{CMD_SUFFIX}', f'pquzm{CMD_SUFFIX}', f'pqbzipmirror{CMD_SUFFIX}', f'pqzm{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'pytdlzip{CMD_SUFFIX}', f'pyz{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'punzipleech{CMD_SUFFIX}', f'puzl{CMD_SUFFIX}', f'pzipleech{CMD_SUFFIX}', f'zl{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'pqbunzipleech{CMD_SUFFIX}', f'pquzl{CMD_SUFFIX}', f'pqbzipleech{CMD_SUFFIX}', f'pqzl{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'pytdlzipleech{CMD_SUFFIX}', f'pyzl{CMD_SUFFIX}'])
        self.CloneCommand = [f'pclone{CMD_SUFFIX}', f'c{CMD_SUFFIX}']
        self.CountCommand = f'pcount{CMD_SUFFIX}'
        self.DeleteCommand = f'pdel{CMD_SUFFIX}'
        self.CancelMirror = f'pcancel{CMD_SUFFIX}'
        self.CancelAllCommand = [f'pcancelall{CMD_SUFFIX}', 'cancellallbot']
        self.ListCommand = f'plist{CMD_SUFFIX}'
        self.SearchCommand = f'psearch{CMD_SUFFIX}'
        self.StatusCommand = [f'pstatus{CMD_SUFFIX}', f's{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'pusers{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'pauthorize{CMD_SUFFIX}', f'a{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'punauthorize{CMD_SUFFIX}', f'ua{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'pblacklist{CMD_SUFFIX}', f'bl{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'prmblacklist{CMD_SUFFIX}', f'rbl{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'pping{CMD_SUFFIX}', f'p{CMD_SUFFIX}']
        self.RestartCommand = [f'prestart{CMD_SUFFIX}', f'r{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'stats{CMD_SUFFIX}', f'st{CMD_SUFFIX}']
        self.HelpCommand = f'phelp{CMD_SUFFIX}'
        self.LogCommand = f'plog{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand = [f'pbsetting{CMD_SUFFIX}', f'bs{CMD_SUFFIX}']
        self.UserSetCommand = [f'pusetting{CMD_SUFFIX}', f'us{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel{CMD_SUFFIX}'
        self.CategorySelect = f'ctsel{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtest{CMD_SUFFIX}', f'sp{CMD_SUFFIX}']
        self.RssCommand = f'rss{CMD_SUFFIX}'
        self.LoginCommand = 'login'
        self.AddImageCommand = f'addimg{CMD_SUFFIX}'
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.IMDBCommand = f'imdb{CMD_SUFFIX}'
        self.AniListCommand = f'anime{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'animehelp{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'mediainfo{CMD_SUFFIX}', f'mi{CMD_SUFFIX}']
        self.MyDramaListCommand = f'mdl{CMD_SUFFIX}'
        self.GDCleanCommand = [f'gdclean{CMD_SUFFIX}', f'gc{CMD_SUFFIX}']
        self.BroadcastCommand = [f'broadcast{CMD_SUFFIX}', f'bc{CMD_SUFFIX}']

BotCommands = _BotCommands()
