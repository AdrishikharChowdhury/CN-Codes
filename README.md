# Computer Networks — ARQ Protocol Simulations

A collection of Automatic Repeat reQuest (ARQ) protocol simulations implemented in Python, each demonstrating a different error control technique over an unreliable channel.

## Projects

| Directory | Protocol | Description |
|---|---|---|
| `stop_wait/` | Stop-and-Wait | Simplest ARQ — send one frame, wait for ACK, retransmit on timeout. |
| `go_back_n/` | Go-Back-N | Sliding window — on loss, retransmit all unacknowledged frames. |
| `selective_repeat/` | Selective Repeat | Sliding window — only retransmit lost/timed-out frames; receiver buffers out-of-order. |
| `crcgen/` | CRC Generator | Cyclic Redundancy Check encoder. |
| `crcdecode/` | CRC Decoder | Cyclic Redundancy Check decoder/verifier. |
| `hostip/` | Host IP | IP address utility. |
| `ipconfig/` | IP Config | Network configuration utility. |
| `ipinfo/` | IP Info | IP information lookup. |

## Common Simulation Parameters

Configurable in each protocol's `models.py`:

- **Window size**: number of outstanding frames
- **Timeout**: seconds before retransmission
- **Packet loss probability**: chance a frame is dropped
- **ACK loss probability**: chance an ACK is dropped
- **Corruption probability**: chance a frame is corrupted in transit
