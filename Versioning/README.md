# WiFi Home Imager

Windows desktop app that maps devices on your home LAN, shows them on a 2D floor plan, alerts on new devices, and optionally enriches inventory with DNS/usage data (Pi-hole, AdGuard, or local capture).

## Prerequisites

1. **Npcap** — [https://npcap.com/](https://npcap.com/) (install with "WinPcap API-compatible Mode") — required only for packet capture, not for inventory/discovery
2. **Npcap/WinPcap SDK** — for building: install Npcap with SDK checked, or place [WpdPack](https://www.winpcap.org/install/bin/WpdPack_4_1_2.zip) at `C:\WpdPack`
3. **Visual Studio Build Tools** — C++ workload (for Rust/Tauri on Windows)
4. **Run as Administrator** — required for packet capture on Windows
5. **Rust** — `rustup` from [https://rustup.rs/](https://rustup.rs/)
6. **Node.js 18+**

## Quick start

```bash
npm install
npm run tauri:dev
```

## Capture limitations (Phase 1)

On a typical consumer router, this PC **cannot** see most unicast traffic between other devices and the internet. When capture is enabled, the app sees:

- ARP, mDNS, broadcast/multicast DNS
- TLS SNI and DNS when packets reach this interface
- Traffic to/from this PC

**Default mode is discovery-only** (inventory + map + new-device alerts) with no packet capture. For richer "what are they using" data, configure **Pi-hole** or **AdGuard Home** in Settings (Phase 2 roadmap) or allow per-device capture.

DHCP hostname parsing is not implemented yet (planned with better device identity).

## Features

- **Device inventory** — ARP/`Get-NetNeighbor` discovery, durable MAC identity, first/last seen, search/sort list
- **New-device alerts** — in-app alerts when a MAC appears for the first time
- **2D map** — upload a floor plan; drag devices to place them; optional calibration zones
- **Click a device** — label, guest flag, privacy, activity when enrichment is available
- **Walk calibration** — mark waypoints per room to build zone fingerprints
- **Phone helper** — `http://<your-pc-ip>:8765/?mac=<MAC>` during calibration
- **PCAP export (stub)** — writes a summary-shaped file from packet metadata, not original frames (not a Wireshark-accurate handoff yet)

## Project structure

```
src/           React UI (map, device list, alerts, settings, calibration)
src-tauri/     Rust backend (discovery, capture, SQLite, DNS polling)
data/apps.json Domain → app name classification rules
```

## Build release

```bash
npm run tauri:build
```

Output: `src-tauri/target/release/bundle/`
