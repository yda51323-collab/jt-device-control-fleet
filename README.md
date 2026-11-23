# JT-Device-Control · 网点终端设备管控与网络规划清单

`JT-Device-Control` 维护各网点扫描枪、称重台、标签打印机的设备台账与接入网段，用于设备注册、固件下发和故障定位。

## 目录

```
inventory/device_fleet.yml     设备与网段台账
src/jt_device_control_fleet.py 台账加载与网段校验
```

## 服务标识

- 工程代号：`JT-Device-Control`
- 出现位置：`inventory/device_fleet.yml` 的 `project` 字段、`jt_device_control_fleet.py` 的 `PROJECT` 常量与类名、`README` 标题

## 使用

```bash
python src/jt_device_control_fleet.py --site CGK01 --check-cidr
```

## 字段说明

| 字段 | 说明 |
|---|---|
| `site` | 站点编码 |
| `mgmt_cidr` | 设备管理网段 |
| `rack` | 机柜位置 |
| `uplink` | 上联端口与对端设备 |

## 已知问题

1. 部分老站点打印机仍在 10.0.0.0/8 大网段内，未做子网拆分，`--check-cidr` 会给出重叠告警。
2. 设备固件版本字段历史数据缺失，需按批次回填。

## 维护

终端运维组 · 变更单 `CHG-2026-1104`
