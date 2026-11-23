# -*- coding: utf-8 -*-
"""JT-Device-Control 设备台账加载与网段校验。"""
import ipaddress
import os

PROJECT = "JT-Device-Control"
TAG = "JT-Device-Control/fleet-checker"
INVENTORY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         "inventory", "device_fleet.yml")


class JtDeviceControlFleet:
    """网点终端设备台账。"""

    def __init__(self, sites):
        self.sites = sites

    def check_cidr(self):
        nets = []
        warns = []
        for s in self.sites:
            net = ipaddress.ip_network(s["mgmt_cidr"], strict=False)
            for prev in nets:
                if net.overlaps(prev):
                    warns.append("overlap: %s <-> %s" % (s["site"], prev))
            nets.append(net)
        return warns


def load_sites(path=INVENTORY):
    """读取 yml 台账（仅解析 sites 段，保持零外部依赖）。"""
    sites, cur, in_sites = [], None, False
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("sites:"):
                in_sites = True
                continue
            if not in_sites:
                continue
            if line.startswith("  - site:"):
                cur = {"site": line.split(":", 1)[1].strip()}
                sites.append(cur)
            elif cur is not None and line.strip().startswith("mgmt_cidr:"):
                cur["mgmt_cidr"] = line.split(":", 1)[1].strip()
    return sites


if __name__ == "__main__":
    fleet = JtDeviceControlFleet(load_sites())
    print(TAG, PROJECT, "sites=%d" % len(fleet.sites))
    for w in fleet.check_cidr():
        print(w)
