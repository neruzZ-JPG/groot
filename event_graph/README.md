# event map
## 同一service内：
service metric -> span metric -> cpu/memory/gc metric
span metric -> span metric(if in span topology)
## 不同service之间：
service metric -> service metric (if in service topology)
span metric -> span metric (if in span topology)