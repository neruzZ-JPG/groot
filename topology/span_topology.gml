graph [
  directed 1
  node [
    id 0
    label "frontend-web:HTTP GET"
  ]
  node [
    id 1
    label "frontendproxy:ingress"
  ]
  node [
    id 2
    label "frontendproxy:router frontend egress"
  ]
  node [
    id 3
    label "frontend:GET"
  ]
  node [
    id 4
    label "frontend:GET /api/currency"
  ]
  node [
    id 5
    label "frontend:executing api route (pages) /api/currency"
  ]
  node [
    id 6
    label "frontend:grpc.oteldemo.CurrencyService/GetSupportedCurrencies"
  ]
  node [
    id 7
    label "currencyservice:CurrencyService/GetSupportedCurrencies"
  ]
  node [
    id 8
    label "loadgenerator:POST"
  ]
  node [
    id 9
    label "frontend:POST"
  ]
  node [
    id 10
    label "frontend:GET /api/recommendations"
  ]
  node [
    id 11
    label "frontend:executing api route (pages) /api/recommendations"
  ]
  node [
    id 12
    label "frontend:grpc.oteldemo.RecommendationService/ListRecommendations"
  ]
  node [
    id 13
    label "recommendationservice:/oteldemo.RecommendationService/ListRecommendations"
  ]
  node [
    id 14
    label "recommendationservice:get_product_list"
  ]
  node [
    id 15
    label "recommendationservice:/schema.v1.Service/ResolveBoolean"
  ]
  node [
    id 16
    label "flagd:schema.v1.Service/ResolveBoolean"
  ]
  node [
    id 17
    label "flagd:resolveBoolean"
  ]
  node [
    id 18
    label "recommendationservice:/oteldemo.ProductCatalogService/ListProducts"
  ]
  node [
    id 19
    label "productcatalogservice:oteldemo.ProductCatalogService/ListProducts"
  ]
  node [
    id 20
    label "frontend:grpc.oteldemo.ProductCatalogService/GetProduct"
  ]
  node [
    id 21
    label "productcatalogservice:oteldemo.ProductCatalogService/GetProduct"
  ]
  node [
    id 22
    label "frontend:grpc.oteldemo.CurrencyService/Convert"
  ]
  node [
    id 23
    label "currencyservice:CurrencyService/Convert"
  ]
  node [
    id 24
    label "frontend:GET /api/cart"
  ]
  node [
    id 25
    label "frontend:executing api route (pages) /api/cart"
  ]
  node [
    id 26
    label "frontend:grpc.oteldemo.CartService/GetCart"
  ]
  node [
    id 27
    label "cartservice:POST /oteldemo.CartService/GetCart"
  ]
  node [
    id 28
    label "cartservice:HGET"
  ]
  node [
    id 29
    label "frontend:POST /api/cart"
  ]
  node [
    id 30
    label "frontend:grpc.oteldemo.CartService/AddItem"
  ]
  node [
    id 31
    label "cartservice:POST /oteldemo.CartService/AddItem"
  ]
  node [
    id 32
    label "cartservice:HMSET"
  ]
  node [
    id 33
    label "cartservice:EXPIRE"
  ]
  node [
    id 34
    label "loadgenerator:GET"
  ]
  node [
    id 35
    label "flagd:flagd.evaluation.v1.Service/ResolveBoolean"
  ]
  node [
    id 36
    label "frontend-web:HTTP POST"
  ]
  node [
    id 37
    label "frontendproxy:router flagservice egress"
  ]
  node [
    id 38
    label "flagd:flagd.evaluation.v1.Service/ResolveAll"
  ]
  node [
    id 39
    label "flagd:resolveAll"
  ]
  node [
    id 40
    label "flagd:schema.v1.Service/ResolveInt"
  ]
  node [
    id 41
    label "flagd:resolveInt"
  ]
  node [
    id 42
    label "frontendproxy:router imageprovider egress"
  ]
  node [
    id 43
    label "imageprovider:imageprovider"
  ]
  node [
    id 44
    label "frontend-web:documentLoad"
  ]
  node [
    id 45
    label "frontend-web:resourceFetch"
  ]
  node [
    id 46
    label "frontend-web:documentFetch"
  ]
  node [
    id 47
    label "frontend:GET /api/products/{productId}"
  ]
  node [
    id 48
    label "frontend:executing api route (pages) /api/products/[productId]"
  ]
  node [
    id 49
    label "frontend:GET /"
  ]
  node [
    id 50
    label "frontend:render route (pages) /"
  ]
  node [
    id 51
    label "frontend:resolve page components"
  ]
  node [
    id 52
    label "frontendproxy:router jaeger egress"
  ]
  node [
    id 53
    label "jaeger-all-in-one:/api/traces"
  ]
  node [
    id 54
    label "frontend:GET /api/data"
  ]
  node [
    id 55
    label "frontend:executing api route (pages) /api/data"
  ]
  node [
    id 56
    label "frontend:grpc.oteldemo.AdService/GetAds"
  ]
  node [
    id 57
    label "adservice:oteldemo.AdService/GetAds"
  ]
  node [
    id 58
    label "adservice:getAdsByCategory"
  ]
  node [
    id 59
    label "adservice:getRandomAds"
  ]
  node [
    id 60
    label "frontend:POST /api/checkout"
  ]
  node [
    id 61
    label "frontend:executing api route (pages) /api/checkout"
  ]
  node [
    id 62
    label "frontend:grpc.oteldemo.CheckoutService/PlaceOrder"
  ]
  node [
    id 63
    label "checkoutservice:oteldemo.CheckoutService/PlaceOrder"
  ]
  node [
    id 64
    label "checkoutservice:oteldemo.PaymentService/Charge"
  ]
  node [
    id 65
    label "paymentservice:grpc.oteldemo.PaymentService/Charge"
  ]
  node [
    id 66
    label "paymentservice:charge"
  ]
  node [
    id 67
    label "checkoutservice:oteldemo.ShippingService/ShipOrder"
  ]
  node [
    id 68
    label "shippingservice:oteldemo.ShippingService/ShipOrder"
  ]
  node [
    id 69
    label "checkoutservice:oteldemo.CartService/EmptyCart"
  ]
  node [
    id 70
    label "cartservice:POST /oteldemo.CartService/EmptyCart"
  ]
  node [
    id 71
    label "cartservice:flagd.evaluation.v1.Service/ResolveBoolean"
  ]
  node [
    id 72
    label "cartservice:POST"
  ]
  node [
    id 73
    label "checkoutservice:prepareOrderItemsAndShippingQuoteFromCart"
  ]
  node [
    id 74
    label "checkoutservice:oteldemo.ProductCatalogService/GetProduct"
  ]
  node [
    id 75
    label "checkoutservice:oteldemo.CartService/GetCart"
  ]
  node [
    id 76
    label "checkoutservice:oteldemo.CurrencyService/Convert"
  ]
  node [
    id 77
    label "checkoutservice:oteldemo.ShippingService/GetQuote"
  ]
  node [
    id 78
    label "shippingservice:oteldemo.ShippingService/GetQuote"
  ]
  node [
    id 79
    label "shippingservice:POST"
  ]
  node [
    id 80
    label "quoteservice:POST /getquote"
  ]
  node [
    id 81
    label "quoteservice:{closure}"
  ]
  node [
    id 82
    label "quoteservice:calculate-quote"
  ]
  node [
    id 83
    label "checkoutservice:orders publish"
  ]
  node [
    id 84
    label "frauddetectionservice:orders process"
  ]
  node [
    id 85
    label "frauddetectionservice:resolve"
  ]
  node [
    id 86
    label "flagd:flagd.evaluation.v1.Service/ResolveInt"
  ]
  node [
    id 87
    label "frauddetectionservice:flagd.evaluation.v1.Service/ResolveInt"
  ]
  node [
    id 88
    label "checkoutservice:HTTP POST"
  ]
  node [
    id 89
    label "emailservice:POST /send_order_confirmation"
  ]
  node [
    id 90
    label "emailservice:send_email"
  ]
  node [
    id 91
    label "emailservice:sinatra.render_template"
  ]
  node [
    id 92
    label "frontend:GET /cart"
  ]
  node [
    id 93
    label "frontend:render route (pages) /cart"
  ]
  node [
    id 94
    label "jaeger-all-in-one:/api/services/{service}/operations"
  ]
  node [
    id 95
    label "jaeger-all-in-one:/api/services"
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 1
    target 2
  ]
  edge [
    source 1
    target 37
  ]
  edge [
    source 1
    target 42
  ]
  edge [
    source 1
    target 52
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 2
    target 9
  ]
  edge [
    source 3
    target 4
  ]
  edge [
    source 3
    target 10
  ]
  edge [
    source 3
    target 24
  ]
  edge [
    source 3
    target 47
  ]
  edge [
    source 3
    target 49
  ]
  edge [
    source 3
    target 54
  ]
  edge [
    source 3
    target 92
  ]
  edge [
    source 4
    target 5
  ]
  edge [
    source 5
    target 6
  ]
  edge [
    source 6
    target 7
  ]
  edge [
    source 8
    target 1
  ]
  edge [
    source 9
    target 29
  ]
  edge [
    source 9
    target 60
  ]
  edge [
    source 10
    target 11
  ]
  edge [
    source 11
    target 12
  ]
  edge [
    source 11
    target 20
  ]
  edge [
    source 11
    target 22
  ]
  edge [
    source 12
    target 13
  ]
  edge [
    source 13
    target 14
  ]
  edge [
    source 14
    target 15
  ]
  edge [
    source 14
    target 18
  ]
  edge [
    source 15
    target 16
  ]
  edge [
    source 16
    target 17
  ]
  edge [
    source 17
    target 17
  ]
  edge [
    source 18
    target 19
  ]
  edge [
    source 20
    target 21
  ]
  edge [
    source 22
    target 23
  ]
  edge [
    source 24
    target 25
  ]
  edge [
    source 25
    target 26
  ]
  edge [
    source 25
    target 30
  ]
  edge [
    source 26
    target 27
  ]
  edge [
    source 27
    target 28
  ]
  edge [
    source 29
    target 25
  ]
  edge [
    source 30
    target 31
  ]
  edge [
    source 31
    target 28
  ]
  edge [
    source 31
    target 32
  ]
  edge [
    source 31
    target 33
  ]
  edge [
    source 34
    target 1
  ]
  edge [
    source 35
    target 17
  ]
  edge [
    source 36
    target 1
  ]
  edge [
    source 37
    target 38
  ]
  edge [
    source 38
    target 39
  ]
  edge [
    source 39
    target 39
  ]
  edge [
    source 40
    target 41
  ]
  edge [
    source 41
    target 41
  ]
  edge [
    source 42
    target 43
  ]
  edge [
    source 44
    target 45
  ]
  edge [
    source 44
    target 46
  ]
  edge [
    source 47
    target 48
  ]
  edge [
    source 48
    target 20
  ]
  edge [
    source 49
    target 50
  ]
  edge [
    source 49
    target 51
  ]
  edge [
    source 52
    target 53
  ]
  edge [
    source 52
    target 94
  ]
  edge [
    source 52
    target 95
  ]
  edge [
    source 54
    target 55
  ]
  edge [
    source 55
    target 56
  ]
  edge [
    source 56
    target 57
  ]
  edge [
    source 57
    target 58
  ]
  edge [
    source 57
    target 59
  ]
  edge [
    source 60
    target 61
  ]
  edge [
    source 61
    target 62
  ]
  edge [
    source 61
    target 20
  ]
  edge [
    source 62
    target 63
  ]
  edge [
    source 63
    target 64
  ]
  edge [
    source 63
    target 67
  ]
  edge [
    source 63
    target 69
  ]
  edge [
    source 63
    target 73
  ]
  edge [
    source 63
    target 83
  ]
  edge [
    source 63
    target 88
  ]
  edge [
    source 64
    target 65
  ]
  edge [
    source 65
    target 66
  ]
  edge [
    source 67
    target 68
  ]
  edge [
    source 69
    target 70
  ]
  edge [
    source 70
    target 71
  ]
  edge [
    source 70
    target 32
  ]
  edge [
    source 70
    target 33
  ]
  edge [
    source 71
    target 72
  ]
  edge [
    source 72
    target 35
  ]
  edge [
    source 73
    target 74
  ]
  edge [
    source 73
    target 75
  ]
  edge [
    source 73
    target 76
  ]
  edge [
    source 73
    target 77
  ]
  edge [
    source 74
    target 21
  ]
  edge [
    source 75
    target 27
  ]
  edge [
    source 76
    target 23
  ]
  edge [
    source 77
    target 78
  ]
  edge [
    source 78
    target 79
  ]
  edge [
    source 79
    target 80
  ]
  edge [
    source 80
    target 81
  ]
  edge [
    source 81
    target 82
  ]
  edge [
    source 83
    target 84
  ]
  edge [
    source 84
    target 85
  ]
  edge [
    source 85
    target 86
  ]
  edge [
    source 85
    target 87
  ]
  edge [
    source 86
    target 41
  ]
  edge [
    source 88
    target 89
  ]
  edge [
    source 89
    target 90
  ]
  edge [
    source 90
    target 91
  ]
  edge [
    source 91
    target 91
  ]
  edge [
    source 92
    target 51
  ]
  edge [
    source 92
    target 93
  ]
]
