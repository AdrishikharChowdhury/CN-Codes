# Stop-and-Wait ARQ Implementation

Simple implementation of the Stop-and-Wait protocol with simulated frame/ACK loss.

## Algorithm (Pseudocode)

### Sender
```text
NextSeqNum = 0
for each message:
    repeat:
        send(message, NextSeqNum)
        wait for event:
            if ACK(NextSeqNum) received:
                NextSeqNum = 1 - NextSeqNum
                break // success
            if timeout:
                continue // retransmit
```

### Receiver
```text
ExpectedSeqNum = 0
loop:
    wait for frame(seq, data)
    if seq == ExpectedSeqNum:
        accept(data)
        send ACK(seq)
        ExpectedSeqNum = 1 - ExpectedSeqNum
    else:
        send ACK(1 - ExpectedSeqNum) // duplicate
```

## Project Structure
- `main.py`: Transmission controller.
- `sender.py`: Sender logic + simulated channel loss.
- `receiver.py`: Receiver logic + duplicate detection.

## How to Run
```bash
python main.py
```
