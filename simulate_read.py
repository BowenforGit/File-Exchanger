import glob
import json
import os
import sys
import time

'''
    Read DAG updates, format it and print to console
'''
end = False

def read_dag_update(timestamp):
    global end
    fname = glob.glob("./grasper-demo-log/*.dag")[0]
    with open(fname, "r") as json_file:
        data = json.load(json_file) # data is a list of updates

    update_dic = dict()
    for upd in data:
        if update_dic.has_key(upd["step"]):
            update_dic[upd["step"]] += 1
        else:
            update_dic[upd["step"]] = 1

    activer = []
    for key, value in update_dic.items():
        tmp = { "steps" : key, "threads" : value }
        activer.append(tmp)

    res = dict()
    res["activer"] = activer
    res["status"] = 0

    if os.path.exists("./grasper-demo-log/{}.result".format(timestamp)):
        res["status"] = 1
        end = True

    print("DAG Updates!")
    print(res)

'''
    Read the output on the client's console
'''
def read_console_output():
    fname = "./grasper-demo-log/client_output.txt"
    res = dict()
    res["content"] = []

    with open(fname, "r") as f:
        for line in f.readlines():
            line = line.rstrip()
            res["content"].append(line)

    print("Client output console updates!")
    print(res)

def read_monitor_stat():
    fname = glob.glob("./grasper-demo-log/*_monitor-data.json")[0]
    with open(fname, "r") as f:
        data = f.readlines()

    res = {"stat" : data}
    print("Monitor data updates!")
    print(res)

def remove_log_files():
    pass


if __name__ == "__main__":
    timestamp = sys.argv[1] # 0 is the script name
    round_cnt = 1
    while True:
        print("====== This is round {} ======".format(str(round_cnt)))
        read_dag_update(timestap)
        read_console_output()
        print("")
        if end:
            break
        time.sleep( 2 )