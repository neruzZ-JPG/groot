graph [
  directed 1
  node [
    id 0
    label "frauddetectionservice:latency_spike &#38; 99"
  ]
  node [
    id 1
    label "frauddetectionservice:latency_spike &#38; 99:orders process"
  ]
  node [
    id 2
    label "frontendproxy:latency_spike &#38; average"
  ]
  node [
    id 3
    label "frontendproxy:tps_spike &#38; rate:router grafana egress"
  ]
  node [
    id 4
    label "frontendproxy:latency_spike &#38; 99:router grafana egress"
  ]
  node [
    id 5
    label "frontendproxy:latency_spike &#38; 95:router grafana egress"
  ]
  node [
    id 6
    label "frontendproxy:latency_spike &#38; average:router grafana egress"
  ]
  node [
    id 7
    label "recommendationservice:latency_spike &#38; average"
  ]
  node [
    id 8
    label "recommendationservice:error &#38; error:/schema.v1.Service/ResolveBoolean"
  ]
  node [
    id 9
    label "recommendationservice:latency_spike &#38; average:/schema.v1.Service/ResolveBoolean"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 2
    target 4
  ]
  edge [
    source 2
    target 5
  ]
  edge [
    source 2
    target 6
  ]
  edge [
    source 7
    target 8
  ]
  edge [
    source 7
    target 9
  ]
]
