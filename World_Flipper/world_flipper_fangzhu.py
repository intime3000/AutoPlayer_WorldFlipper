from world_flipper_actions import *

# 选boss建房之后开始，房主退出再重建
def wf_owner(player,loop_time = 0):
    print("[info] 使用设备{0}开始建房...".format(player.use_device))
    if login(player): # 从房间内等人开始执行
        count = 0
        while count < loop_time or loop_time == 0:
            timeout_flag = wait_in_room(player)
            if not timeout_flag: 
                quit_battle(player)
                build_from_multiplayer(player)
            else: # 房间没人来，自动解散
                build_from_multiplayer(player)
            count += 1
            print("{1} [info] 房主已执行{0}次".format(count, datetime.datetime.now()))

    else: # 从启动游戏开始执行
        player.touch((465,809)) # 领主战
        player.wait_touch("button_pickup") # pickup
        time.sleep(2)
        player.touch((366,348)) # 选第一个难度
        count = 0
        build_from_multiplayer(player,change_zhaomu=True)
        while count < loop_time or loop_time == 0:
            timeout_flag = wait_in_room(player)
            if not timeout_flag: 
                quit_battle(player)
                build_from_multiplayer(player)
            else: # 房间没人来，自动解散
                build_from_multiplayer(player)
            count += 1
            print("{1} [info] 房主已执行{0}次".format(count, datetime.datetime.now()))
            
    
if __name__=="__main__":
    player = Autoplayer(use_device=fangzhu_device, adb_path=adb_path,apk_name=wf_apk_name,active_class_name=wf_active_class_name)
    wf_owner(player)