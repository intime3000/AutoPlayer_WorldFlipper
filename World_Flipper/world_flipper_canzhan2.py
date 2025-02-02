from world_flipper_canzhan1 import *

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("./config.ini")

    teamconfig = configparser.ConfigParser()
    teamconfig.read("./teamset.ini")

    event_screenshot = config["RAID"]["event_screenshot"]
    raid_choose = config["RAID"]["raid_choose"]
    timeout = config["WF"].getint("timeout")
    battle_timeout = config["WF"].getint("battle_timeout")
    event_mode = config["RAID"].getint("event_mode")
    team = teamset_from_ini(
        teamconfig=teamconfig, event_mode=event_mode, raid_choose=raid_choose, event_screenshot=event_screenshot
    )
    player = Autoplayer(
        use_device=config["WF"]["canzhan_device_2"],
        adb_path=config["GENERAL"]["adb_path"],
        apk_name=config["WF"]["wf_apk_name"],
        active_class_name=config["WF"]["wf_active_class_name"],
        debug=config["GENERAL"].getint("Debug"),
        accuracy=config["GENERAL"].getfloat("accuracy"),
        screenshot_blank=config["GENERAL"].getfloat("screenshot_blank"),
        wanted_path=config["GENERAL"]["wanted_path"],
    )
    count = 0
    while True:
        count = wf_join(
            player,
            count=count,
            event_mode=event_mode,
            timeout=timeout,
            battle_timeout=battle_timeout,
            team=team,
        )
        player.stop_app()
        time.sleep(3)
