import json
from pathlib import Path

# Load existing products to copy and enrich them
existing_products = [
  {
    "@type": "Product",
    "productID": "BISC-001",
    "name": "Chocochip Cookies",
    "sku": "COOKIES-001",
    "image": ["http://localhost:10999/images/cookies.jpg"],
    "brand": {
      "@type": "Brand",
      "name": "CookieCo"
    },
    "offers": {
      "price": "4.99",
      "priceCurrency": "USD",
      "priceSpecification": None,
      "@type": "Offer",
      "availability": "https://schema.org/InStock",
      "itemCondition": "https://schema.org/NewCondition"
    },
    "aggregateRating": None,
    "url": "https://example.com/bisc-001",
    "description": "Fresly baked Chocochip Cookies",
    "gtin": "9876543210125",
    "mpn": "CC-SB-001",
    "category": "Groceries > Snacks > Cookies & Biscuits",
    "nutrition": {
      "servingSize": "30g",
      "calories": 150,
      "totalFat": "7g",
      "saturatedFat": "4g",
      "sodium": "95mg",
      "totalCarbohydrates": "20g",
      "dietaryFiber": "1g",
      "sugars": "12g",
      "protein": "2g"
    }
  },
  {
    "@type": "Product",
    "productID": "STRAW-001",
    "name": "Fresh Strawberries",
    "sku": "STRAW-001",
    "image": ["http://localhost:10999/images/strawberries.jpg"],
    "brand": {
      "@type": "Brand",
      "name": "FarmFresh"
    },
    "offers": {
      "price": "4.49",
      "priceCurrency": "USD",
      "priceSpecification": None,
      "@type": "Offer",
      "availability": "https://schema.org/InStock",
      "itemCondition": "https://schema.org/NewCondition"
    },
    "aggregateRating": None,
    "url": "https://example.com/straw-001",
    "description": "Sweet and juicy fresh strawberries, 1 lb.",
    "gtin": "9876543210127",
    "mpn": "FF-ST-001",
    "category": "Groceries > Fresh Produce > Fruits",
    "nutrition": {
      "servingSize": "140g",
      "calories": 45,
      "totalFat": "0g",
      "saturatedFat": "0g",
      "sodium": "0mg",
      "totalCarbohydrates": "11g",
      "dietaryFiber": "3g",
      "sugars": "7g",
      "protein": "1g"
    }
  },
  {
    "@type": "Product",
    "productID": "CHIPS-001",
    "name": "Classic Potato Chips",
    "sku": "CHIPS-001",
    "image": ["http://localhost:10999/images/chips.jpg"],
    "brand": {
      "@type": "Brand",
      "name": "SaltySnacks"
    },
    "offers": {
      "price": "3.79",
      "priceCurrency": "USD",
      "priceSpecification": None,
      "@type": "Offer",
      "availability": "https://schema.org/InStock",
      "itemCondition": "https://schema.org/NewCondition"
    },
    "aggregateRating": None,
    "url": "https://example.com/chips-001",
    "description": "Crispy and salty classic potato chips, family size.",
    "gtin": "9876543210128",
    "mpn": "SS-PC-001",
    "category": "Groceries > Snacks > Chips & Crisps",
    "nutrition": {
      "servingSize": "28g",
      "calories": 150,
      "totalFat": "10g",
      "saturatedFat": "1.5g",
      "sodium": "170mg",
      "totalCarbohydrates": "15g",
      "dietaryFiber": "1g",
      "sugars": "0g",
      "protein": "2g"
    }
  },
  {
    "@type": "Product",
    "productID": "SW-CHIPS-001",
    "name": "Baked Sweet Potato Chips",
    "sku": "SW-CHIPS-001",
    "image": ["http://localhost:10999/images/chips.jpg"],
    "brand": {
      "@type": "Brand",
      "name": "SaltySnacks"
    },
    "offers": {
      "price": "4.79",
      "priceCurrency": "USD",
      "priceSpecification": None,
      "@type": "Offer",
      "availability": "https://schema.org/InStock",
      "itemCondition": "https://schema.org/NewCondition"
    },
    "aggregateRating": None,
    "url": "https://example.com/sw-chips-001",
    "description": "Crispy and salty sweet potato chips, family size.",
    "gtin": "9876543210129",
    "mpn": "SS-PC-009",
    "category": "Groceries > Snacks > Chips & Crisps",
    "nutrition": {
      "servingSize": "28g",
      "calories": 130,
      "totalFat": "4g",
      "saturatedFat": "0.5g",
      "sodium": "140mg",
      "totalCarbohydrates": "21g",
      "dietaryFiber": "3g",
      "sugars": "6g",
      "protein": "2g"
    }
  },
  {
    "@type": "Product",
    "productID": "O-COOKIES-001",
    "name": "Classic Oat Cookies",
    "sku": "O-COOKIES-001",
    "image": ["http://localhost:10999/images/oat_cookies.jpg"],
    "brand": {
      "@type": "Brand",
      "name": "CookieCo"
    },
    "offers": {
      "price": "5.99",
      "priceCurrency": "USD",
      "priceSpecification": None,
      "@type": "Offer",
      "availability": "https://schema.org/InStock",
      "itemCondition": "https://schema.org/NewCondition"
    },
    "aggregateRating": None,
    "url": "https://example.com/bisc-001",
    "description": "Fresly baked Oat Cookies",
    "gtin": "9876543210129",
    "mpn": "CC-SB1-001",
    "category": "Groceries > Snacks > Cookies & Biscuits",
    "nutrition": {
      "servingSize": "35g",
      "calories": 160,
      "totalFat": "6g",
      "saturatedFat": "2.5g",
      "sodium": "110mg",
      "totalCarbohydrates": "23g",
      "dietaryFiber": "2g",
      "sugars": "9g",
      "protein": "3g"
    }
  },
  {
    "@type": "Product",
    "productID": "NUTRIBAR-001",
    "name": "Nutri-Bar",
    "sku": "NUTRIBAR-001",
    "image": ["http://localhost:10999/images/nutribar.jpg"],
    "brand": {
      "@type": "Brand",
      "name": "HealthEats"
    },
    "offers": {
      "price": "2.99",
      "priceCurrency": "USD",
      "priceSpecification": None,
      "@type": "Offer",
      "availability": "https://schema.org/InStock",
      "itemCondition": "https://schema.org/NewCondition"
    },
    "aggregateRating": None,
    "url": "https://example.com/nutribar-001",
    "description": "A healthy and nutritious snack bar, packed with nuts and seeds.",
    "gtin": "9876543210135",
    "mpn": "HE-NB-001",
    "category": "Groceries > Health & Nutrition Bars",
    "nutrition": {
      "servingSize": "40g",
      "calories": 180,
      "totalFat": "8g",
      "saturatedFat": "1.5g",
      "sodium": "80mg",
      "totalCarbohydrates": "22g",
      "dietaryFiber": "4g",
      "sugars": "8g",
      "protein": "5g"
    }
  }
]

# Helper function to generate Unsplash URLs
def unsplash_img(photo_id):
  return [f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w=600&q=80"]

new_products_specs = [
  # --- FOOD & BEVERAGES (with nutrition tables) ---
  {
    "category": "Groceries > Dairy & Alternatives",
    "brand": "DairyGold",
    "items": [
      ("Organic Whole Milk", "MILK-001", "1 Gallon Organic Whole Milk", "3.99", "photo-1550583724-b2692b85b150", {
        "servingSize": "240ml", "calories": 150, "totalFat": "8g", "saturatedFat": "5g", "sodium": "120mg", "totalCarbohydrates": "12g", "dietaryFiber": "0g", "sugars": "12g", "protein": "8g"
      }),
      ("Organic Almond Milk", "ALM-MILK-001", "Unsweetened Vanilla Almond Milk", "3.49", "photo-1553456558-aff63285bdd1", {
        "servingSize": "240ml", "calories": 30, "totalFat": "2.5g", "saturatedFat": "0g", "sodium": "160mg", "totalCarbohydrates": "1g", "dietaryFiber": "1g", "sugars": "0g", "protein": "1g"
      }),
      ("Greek Yogurt Plain", "GYOG-001", "Non-fat Plain Greek Yogurt, 32 oz", "5.49", "photo-1488477181946-6428a0291777", {
        "servingSize": "170g", "calories": 100, "totalFat": "0g", "saturatedFat": "0g", "sodium": "60mg", "totalCarbohydrates": "6g", "dietaryFiber": "0g", "sugars": "6g", "protein": "18g"
      }),
      ("Cheddar Cheese Block", "CHED-001", "Sharp Cheddar Cheese block, 8 oz", "4.29", "photo-1618164435735-413d3b066c9a", {
        "servingSize": "28g", "calories": 110, "totalFat": "9g", "saturatedFat": "5g", "sodium": "180mg", "totalCarbohydrates": "1g", "dietaryFiber": "0g", "sugars": "0g", "protein": "7g"
      })
    ]
  },
  {
    "category": "Groceries > Pantry > Spreads & Condiments",
    "brand": "NutriSpread",
    "items": [
      ("Creamy Peanut Butter", "PEANUT-001", "All-natural Creamy Peanut Butter, 16 oz", "4.89", "photo-1590080875515-8a3a8dc5735e", {
        "servingSize": "32g", "calories": 190, "totalFat": "16g", "saturatedFat": "2.5g", "sodium": "140mg", "totalCarbohydrates": "7g", "dietaryFiber": "3g", "sugars": "2g", "protein": "8g"
      }),
      ("Organic Raw Honey", "HONEY-001", "Pure unfiltered raw wildflower honey, 12 oz", "6.99", "photo-1587049352846-4a222e784d38", {
        "servingSize": "21g", "calories": 60, "totalFat": "0g", "saturatedFat": "0g", "sodium": "0mg", "totalCarbohydrates": "17g", "dietaryFiber": "0g", "sugars": "16g", "protein": "0g"
      }),
      ("Extra Virgin Olive Oil", "OIL-001", "Cold-pressed Extra Virgin Olive Oil, 750ml", "12.99", "photo-1474979266404-7eaacbcd87c5", {
        "servingSize": "15ml", "calories": 120, "totalFat": "14g", "saturatedFat": "2g", "sodium": "0mg", "totalCarbohydrates": "0g", "dietaryFiber": "0g", "sugars": "0g", "protein": "0g"
      })
    ]
  },
  {
    "category": "Groceries > Beverages > Tea & Coffee",
    "brand": "BrewPeak",
    "items": [
      ("Organic Green Tea", "GTEA-001", "Sencha Green Tea bags, 20 count", "3.99", "photo-1597481499750-3e6b22637e12", {
        "servingSize": "1 bag", "calories": 0, "totalFat": "0g", "saturatedFat": "0g", "sodium": "0mg", "totalCarbohydrates": "0g", "dietaryFiber": "0g", "sugars": "0g", "protein": "0g"
      }),
      ("Dark Roast Coffee Beans", "COFFEE-001", "Whole Bean Arabica Coffee, 12 oz", "8.99", "photo-1447933601403-0c6688de566e", {
        "servingSize": "1 tbsp", "calories": 2, "totalFat": "0g", "saturatedFat": "0g", "sodium": "5mg", "totalCarbohydrates": "0g", "dietaryFiber": "0g", "sugars": "0g", "protein": "0.2g"
      }),
      ("Matcha Green Tea Powder", "MATCHA-001", "Ceremonial Grade Matcha Powder, 1.05 oz", "19.99", "photo-1536256263959-770b48d82b0a", {
        "servingSize": "2g", "calories": 5, "totalFat": "0g", "saturatedFat": "0g", "sodium": "0mg", "totalCarbohydrates": "1g", "dietaryFiber": "0.5g", "sugars": "0g", "protein": "0.5g"
      })
    ]
  },
  {
    "category": "Groceries > Beverages > Juices & Sodas",
    "brand": "FizzWater",
    "items": [
      ("Sparkling Water Lime", "SWATER-001", "Lime flavored unsweetened sparkling water, 8pk", "4.49", "photo-1603569283847-be4020c22627", {
        "servingSize": "355ml", "calories": 0, "totalFat": "0g", "saturatedFat": "0g", "sodium": "0mg", "totalCarbohydrates": "0g", "dietaryFiber": "0g", "sugars": "0g", "protein": "0g"
      }),
      ("Organic Orange Juice", "OJUICE-001", "No pulp organic orange juice, 52 oz", "5.99", "photo-1613478223719-2ab802602423", {
        "servingSize": "240ml", "calories": 110, "totalFat": "0g", "saturatedFat": "0g", "sodium": "0mg", "totalCarbohydrates": "26g", "dietaryFiber": "0g", "sugars": "22g", "protein": "2g"
      }),
      ("Ginger Kombucha", "KOMBU-001", "Organic Raw Ginger Kombucha, 16 oz", "3.79", "photo-1594589980197-e89c2add08ef", {
        "servingSize": "473ml", "calories": 60, "totalFat": "0g", "saturatedFat": "0g", "sodium": "10mg", "totalCarbohydrates": "14g", "dietaryFiber": "0g", "sugars": "12g", "protein": "0g"
      }),
      ("Coconut Water Pure", "COCO-001", "100% pure coconut water, 1L", "4.29", "photo-1543362906-acfc16c67564", {
        "servingSize": "240ml", "calories": 45, "totalFat": "0g", "saturatedFat": "0g", "sodium": "40mg", "totalCarbohydrates": "11g", "dietaryFiber": "0g", "sugars": "9g", "protein": "0g"
      })
    ]
  },
  {
    "category": "Groceries > Pantry > Grains & Pasta",
    "brand": "GrainSelect",
    "items": [
      ("Organic Quinoa", "QUINOA-001", "Organic White Quinoa Grain, 16 oz", "5.49", "photo-1586201375761-83865001e31c", {
        "servingSize": "45g", "calories": 170, "totalFat": "2.5g", "saturatedFat": "0g", "sodium": "0mg", "totalCarbohydrates": "29g", "dietaryFiber": "3g", "sugars": "0g", "protein": "6g"
      }),
      ("Rolled Oats", "OATS-001", "100% Whole Grain Rolled Oats, 32 oz", "3.99", "photo-1586444248902-2f64eddc13df", {
        "servingSize": "40g", "calories": 150, "totalFat": "3g", "saturatedFat": "0.5g", "sodium": "0mg", "totalCarbohydrates": "27g", "dietaryFiber": "4g", "sugars": "1g", "protein": "5g"
      }),
      ("Brown Rice", "BRICE-001", "Organic Long Grain Brown Rice, 32 oz", "3.49", "photo-1586201375761-83865001e31c", {
        "servingSize": "45g", "calories": 160, "totalFat": "1.5g", "saturatedFat": "0g", "sodium": "0mg", "totalCarbohydrates": "33g", "dietaryFiber": "2g", "sugars": "0g", "protein": "3g"
      })
    ]
  },
  {
    "category": "Groceries > Snacks > Bars & Sweets",
    "brand": "CocoDelight",
    "items": [
      ("Dark Chocolate Bar 85%", "DKCHOC-001", "Organic Dark Chocolate Bar, 85% Cacao, 3 oz", "3.49", "photo-1548907040-4d42b5212c11", {
        "servingSize": "30g", "calories": 180, "totalFat": "14g", "saturatedFat": "9g", "sodium": "0mg", "totalCarbohydrates": "11g", "dietaryFiber": "3g", "sugars": "4g", "protein": "3g"
      }),
      ("Roasted Almonds Salted", "ALMND-001", "Whole roasted salted almonds, 10 oz", "6.29", "photo-1599599810769-bcde5a160d32", {
        "servingSize": "28g", "calories": 160, "totalFat": "14g", "saturatedFat": "1g", "sodium": "115mg", "totalCarbohydrates": "6g", "dietaryFiber": "3g", "sugars": "1g", "protein": "6g"
      }),
      ("Granola Energy Mix", "GRAN-001", "Crunchy oats and honey granola, 12 oz", "4.99", "photo-1568254183919-78a4f43a2877", {
        "servingSize": "55g", "calories": 240, "totalFat": "7g", "saturatedFat": "1g", "sodium": "75mg", "totalCarbohydrates": "38g", "dietaryFiber": "4g", "sugars": "14g", "protein": "5g"
      })
    ]
  },

  # --- ELECTRONICS (no nutrition tables: nutrition=None) ---
  {
    "category": "Electronics > Audio > Headphones",
    "brand": "SonicWave",
    "items": [
      ("Wireless ANC Headphones", "HP-ANC-001", "Active Noise Cancelling Bluetooth Headphones", "99.99", "photo-1505740420928-5e560c06d30e", None),
      ("True Wireless Earbuds", "EAR-TWS-001", "Sweatproof bluetooth earbuds with charging case", "49.99", "photo-1590658268037-6bf12165a8df", None),
      ("Portable Bluetooth Speaker", "SPK-BT-001", "IPX7 waterproof portable wireless speaker", "39.99", "photo-1608043152269-423dbba4e7e1", None)
    ]
  },
  {
    "category": "Electronics > Computer Accessories",
    "brand": "LogiTech",
    "items": [
      ("Ergonomic Wireless Mouse", "MOU-ERG-001", "Precision wireless mouse with adjustable DPI", "29.99", "photo-1615663245857-ac93bb7c39e7", None),
      ("Mechanical Keyboard RGB", "KBD-RGB-001", "Tactile clicky mechanical keyboard, RGB backlit", "79.99", "photo-1618384887929-16ec33fab9ef", None),
      ("Aluminum Laptop Stand", "LPT-STND-001", "Adjustable ergonomic cooling laptop stand", "24.99", "photo-1527443224154-c4a3942d3acf", None),
      ("USB-C Multiport Hub", "HUB-USBC-001", "7-in-1 USB-C hub with HDMI, SD Reader, 3 USB ports", "34.99", "photo-1547082299-de196ea013d6", None)
    ]
  },
  {
    "category": "Electronics > Power & Smart Home",
    "brand": "VoltPlus",
    "items": [
      ("Fast Charging Power Bank", "PWR-BANK-001", "20000mAh PD fast charging external battery", "39.99", "photo-1609592424109-dd825b413d11", None),
      ("Smart Wi-Fi Plug 4-Pack", "SMT-PLUG-001", "Smart plugs compatible with Alexa and Google Home", "24.99", "photo-1558002038-1055907df827", None),
      ("Fast USB-C Charger 65W", "CHG-65W-001", "Dual port GaN wall charger fast power adapter", "29.99", "photo-1622445262465-2481974e27e1", None)
    ]
  },
  {
    "category": "Electronics > Gadgets",
    "brand": "Chronos",
    "items": [
      ("Smart Fitness Watch", "WATCH-FIT-001", "Heart rate and sleep tracker smart watch, waterproof", "59.99", "photo-1517502884422-41eaaced0168", None),
      ("MagSafe Wireless Charger", "MAG-CHG-001", "15W magnetic alignment fast wireless charging pad", "19.99", "photo-1622445262465-2481974e27e1", None),
      ("Desktop Ring Light", "RNG-LGT-001", "10 inch ring light with tripod stand for video calls", "19.99", "photo-1522071820081-009f0129c71c", None)
    ]
  },

  # --- HOME & KITCHEN ---
  {
    "category": "Home & Kitchen > Kitchen Appliances",
    "brand": "KitchenPro",
    "items": [
      ("Digital Air Fryer", "FRY-AIR-001", "5.8 QT digital air fryer with preset programs", "89.99", "photo-1621972750749-0fbb1abb7736", None),
      ("Electric Gooseneck Kettle", "KET-GOOS-001", "Temperature control electric pour-over kettle", "69.99", "photo-1578643463396-0997cb5328c1", None),
      ("Personal Smoothie Blender", "BLND-SM-001", "High speed personal blender with to-go cup", "34.99", "photo-1578643463396-0997cb5328c1", None),
      ("Automatic Milk Frother", "FROTH-001", "Hot & cold milk frother and warmer", "29.99", "photo-1578643463396-0997cb5328c1", None)
    ]
  },
  {
    "category": "Home & Kitchen > Drinkware & Dining",
    "brand": "HydroVessel",
    "items": [
      ("Insulated Water Bottle", "BTL-VAC-001", "32 oz double-wall vacuum insulated water bottle", "24.99", "photo-1602143407151-7111542de6e8", None),
      ("Ceramic Coffee Mug Set", "MUG-CER-001", "Set of 4 matte ceramic coffee mugs, 12 oz", "18.99", "photo-1514432324607-a09d9b4aefdd", None),
      ("Glass Food Containers", "CONT-GLS-001", "10-piece glass meal prep storage containers", "29.99", "photo-1606787366850-de6330128bfc", None)
    ]
  },
  {
    "category": "Home & Kitchen > Organization & Decor",
    "brand": "CozyHome",
    "items": [
      ("Scented Soy Candle", "CNDL-SOY-001", "Lavender Eucalyptus relaxing aromatherapy candle", "14.99", "photo-1603006905003-be475563bc59", None),
      ("Memory Foam Pillow", "PIL-MEM-001", "Ergonomic contour pillow for neck pain relief", "34.99", "photo-1631679706909-1844bbd07221", None),
      ("Ultrasonic Oil Diffuser", "DIFF-OIL-001", "Essential oil diffuser with 7-color LED lights", "24.99", "photo-1602928321679-560bb453f190", None),
      ("Fleece Throw Blanket", "BLKT-FLC-001", "Super soft cozy plush fleece throw blanket", "19.99", "photo-1580301762395-21ce84d00bc6", None)
    ]
  },

  # --- APPAREL & ACCESSORIES ---
  {
    "category": "Apparel > Men's Clothing",
    "brand": "FitWear",
    "items": [
      ("Cotton Crewneck T-Shirt", "TSH-MN-001", "Pack of 3 premium cotton basic t-shirts", "24.99", "photo-1521572267360-ee0c2909d518", None),
      ("Athletic Jogger Pants", "JOG-MN-001", "Slim fit breathable running joggers", "29.99", "photo-1552374196-1ab2a1c593e8", None),
      ("Running Cushion Socks", "SOX-ATH-001", "6 pairs of low-cut athletic socks with arch support", "14.99", "photo-1582966772680-860e372bb558", None)
    ]
  },
  {
    "category": "Apparel > Accessories",
    "brand": "LuxCarry",
    "items": [
      ("Polarized Sunglasses", "SUN-POL-001", "Classic retro style UV400 polarized sunglasses", "16.99", "photo-1511499767150-a48a237f0083", None),
      ("Slim Leather Wallet", "WLT-LTH-001", "RFID blocking genuine leather bi-fold wallet", "24.99", "photo-1627124118318-7f9999a4c843", None),
      ("Canvas Backpack", "BPK-CNV-001", "Vintage travel school backpack fits 15.6 inch laptop", "39.99", "photo-1553062407-98eeb64c6a62", None),
      ("Winter Knit Beanie", "BN-KNT-001", "Warm acrylic rib-knit beanie hat, unisex", "12.99", "photo-1576871337622-98d48d4aa53e", None)
    ]
  },
  {
    "category": "Apparel > Women's Clothing",
    "brand": "AuraActive",
    "items": [
      ("High Waisted Leggings", "LEG-WM-001", "Buttery soft non-see-through workout leggings", "22.99", "photo-1506152983158-b4a74a01c721", None),
      ("Oversized Knit Sweater", "SWT-WM-001", "Casual crewneck loose pullover sweater", "34.99", "photo-1583743814966-8936f5b7be1a", None),
      ("Packable Rain Jacket", "JKT-RAIN-001", "Waterproof windbreaker lightweight rain coat", "29.99", "photo-1548883354-7622d03aca27", None)
    ]
  },

  # --- FITNESS & OUTDOORS ---
  {
    "category": "Fitness > Home Gym",
    "brand": "FlexGym",
    "items": [
      ("Thick Yoga Mat", "YOGA-MAT-001", "1/2 inch extra thick high density exercise mat", "21.99", "photo-1592432678016-e910b452f9a2", None),
      ("Resistance Bands Set", "BND-RST-001", "Set of 5 stackable exercise bands with handles", "19.99", "photo-1517838277536-f5f99be501cd", None),
      ("Adjustable Dumbbells Pair", "DMB-ADJ-001", "Selectable weight dumbbells pair, 5-25 lbs each", "149.99", "photo-1638536532686-d610adfc8e5c", None),
      ("Foam Roller Roller", "FOAM-ROL-001", "High density foam roller for muscle massage", "14.99", "photo-1600881333168-2ef49b341f30", None)
    ]
  },
  {
    "category": "Outdoors > Camping & Hiking",
    "brand": "TrailBlaze",
    "items": [
      ("Waterproof Camping Tent", "TNT-CAMP-001", "3-Person 4-Season easy setup dome camping tent", "79.99", "photo-1504280390367-361c6d9f38f4", None),
      ("Sleeping Bag 3-Season", "SLP-BAG-001", "Warm weather envelope sleeping bag for camping", "29.99", "photo-1515621061946-eff1c2a352bd", None),
      ("Rechargeable LED Headlamp", "HD-LMP-001", "Super bright waterproof headlamp flashlight", "14.99", "photo-1554178286-db408c69260a", None),
      ("Parachute Hammock Single", "HMC-SNGL-001", "Portable single camping hammock with tree straps", "24.99", "photo-1502082553048-f009c37129b9", None)
    ]
  },

  # --- OFFICE & STATIONERY ---
  {
    "category": "Office > Desk Accessories",
    "brand": "DeskCraft",
    "items": [
      ("Dual-Sided Desk Pad", "MAT-DSK-001", "Large PU leather waterproof desk protector blotter", "15.99", "photo-1585776245991-cf89dd7fc73a", None),
      ("Mesh Desk Organizer", "ORG-DSK-001", "Multi-functional desktop organizer caddy, 6 compartments", "18.99", "photo-1598300042247-d088f8ab3a91", None),
      ("Monitor Stand Riser", "RSR-MON-001", "Wood monitor riser stand with drawer slots", "24.99", "photo-1527443224154-c4a3942d3acf", None)
    ]
  },
  {
    "category": "Office > Notebooks & Pens",
    "brand": "ScriptCo",
    "items": [
      ("Dotted Journal Notebook", "NTB-DOT-001", "A5 hardcover dotted paper bullet journal, 120gsm", "12.99", "photo-1531346878377-a5be20888e57", None),
      ("Fine Gel Pens Set", "PEN-GEL-001", "12 colors fine point gel ink pens, smooth writing", "9.99", "photo-1583485088034-697b5bc54ccd", None),
      ("Sticky Notes Value Pack", "STK-NTE-001", "24 pads pastel colors sticky notes, 3x3 inches", "11.99", "photo-1586075010923-2dd4570fb338", None)
    ]
  },
  {
    "category": "Office > Tech & Equipment",
    "brand": "ShredTech",
    "items": [
      ("Cross-Cut Paper Shredder", "SHRD-PPR-001", "8-sheet cross-cut paper and credit card shredder", "45.99", "photo-1598300042247-d088f8ab3a91", None),
      ("Laminator Machine 9-inch", "LAM-MON-001", "Thermal laminating machine with laminating pouches", "29.99", "photo-1598300042247-d088f8ab3a91", None)
    ]
  }
]

# Build the 100 new products list
generated_products = []
import random

# Start counter for GTIN / MPN to keep them unique and realistic
gtin_base = 9876543210200
mpn_counter = 200

for block in new_products_specs:
  category = block["category"]
  brand_name = block["brand"]
  
  for name, sku, desc, price, photo_id, nutrition in block["items"]:
    gtin = str(gtin_base)
    mpn = f"{brand_name[:2].upper()}-{sku}"
    
    product = {
      "@type": "Product",
      "productID": sku,
      "name": name,
      "sku": sku,
      "image": unsplash_img(photo_id),
      "brand": {
        "@type": "Brand",
        "name": brand_name
      },
      "offers": {
        "price": price,
        "priceCurrency": "USD",
        "priceSpecification": None,
        "@type": "Offer",
        "availability": "https://schema.org/InStock",
        "itemCondition": "https://schema.org/NewCondition"
      },
      "aggregateRating": None,
      "url": f"https://example.com/{sku.lower()}",
      "description": desc,
      "gtin": gtin,
      "mpn": mpn,
      "category": category
    }
    
    if nutrition:
      product["nutrition"] = nutrition
    else:
      product["nutrition"] = None
      
    generated_products.append(product)
    gtin_base += 1
    mpn_counter += 1

# Total products: existing enriched (6) + new generated (55)
# Wait, we need to make sure we have exactly 100 *additional* products!
# Let's count how many we have in new_products_specs.
# DairyGold: 4
# NutriSpread: 3
# BrewPeak: 3
# FizzWater: 4
# GrainSelect: 3
# CocoDelight: 3
# SonicWave: 3
# LogiTech: 4
# VoltPlus: 3
# Chronos: 3
# KitchenPro: 4
# HydroVessel: 3
# CozyHome: 4
# FitWear: 3
# LuxCarry: 4
# AuraActive: 3
# FlexGym: 4
# TrailBlaze: 4
# DeskCraft: 3
# ScriptCo: 3
# ShredTech: 2
# Total generated: 4+3+3+4+3+3+3+4+3+3+4+3+4+3+4+3+4+4+3+3+2 = 69 products.
# We need 100 *additional* products. So we need to add 31 more products to reach 100 additional products!
# Let's define another list of items to add so we have exactly 100 additional products.

extra_products_specs = [
  {
    "category": "Groceries > Pantry > Spices & Seasonings",
    "brand": "SpiceRoute",
    "items": [
      ("Organic Turmeric Powder", "TURM-001", "Ground turmeric root powder, 8 oz", "4.49", "photo-1596003906949-67221c377f6c", {
        "servingSize": "5g", "calories": 15, "totalFat": "0.5g", "saturatedFat": "0g", "sodium": "0mg", "totalCarbohydrates": "3g", "dietaryFiber": "1g", "sugars": "0g", "protein": "0.5g"
      }),
      ("Himalayan Pink Salt", "SALT-PNK-001", "Fine grain Himalayan pink salt, 16 oz", "3.99", "photo-1506368249639-73a05d6f6488", {
        "servingSize": "1.5g", "calories": 0, "totalFat": "0g", "saturatedFat": "0g", "sodium": "570mg", "totalCarbohydrates": "0g", "dietaryFiber": "0g", "sugars": "0g", "protein": "0g"
      }),
      ("Organic Black Pepper", "PEP-BLK-001", "Whole black peppercorns with grinder, 4 oz", "4.99", "photo-1506368249639-73a05d6f6488", {
        "servingSize": "1g", "calories": 0, "totalFat": "0g", "saturatedFat": "0g", "sodium": "0mg", "totalCarbohydrates": "0g", "dietaryFiber": "0g", "sugars": "0g", "protein": "0g"
      })
    ]
  },
  {
    "category": "Home & Kitchen > Gardening & Plants",
    "brand": "GreenThumb",
    "items": [
      ("Succulent Plants 4-Pack", "PLNT-SUC-001", "Assorted live mini succulent plants in pots", "19.99", "photo-1509440159596-0249088772ff", None),
      ("Self Watering Planter", "POT-SLF-001", "Plastic self watering flower pot, 6 inch", "12.99", "photo-1485955900006-10f4d324d411", None),
      ("Organic Potting Soil", "SOIL-ORG-001", "Premium organic potting mix, 8 QT", "9.99", "photo-1485955900006-10f4d324d411", None)
    ]
  },
  {
    "category": "Toys & Games > Board Games & Puzzles",
    "brand": "FunPlay",
    "items": [
      ("Wooden Chess Set", "TOY-CHESS-001", "Handcrafted folding wooden chess board game set", "29.99", "photo-1529699211952-734e80c4d42b", None),
      ("Jigsaw Puzzle 1000 Pcs", "TOY-PZL-001", "High quality cardboard jigsaw puzzle, landscape", "14.99", "photo-1585320806297-9794b3e4eeae", None),
      ("Classic Card Games Set", "TOY-CARD-001", "Pack of 2 standard bicycle playing cards", "6.99", "photo-1585320806297-9794b3e4eeae", None)
    ]
  },
  {
    "category": "Books > Fiction & Literature",
    "brand": "PaperBacks",
    "items": [
      ("Classic Sci-Fi Novel", "BOK-SF-001", "Hardcover collector edition classic sci-fi novel", "19.99", "photo-1543002588-bfa74002ed7e", None),
      ("Aesthetic Notebook Set", "BOK-NTB-002", "Set of 3 minimalist journals, soft cover", "14.99", "photo-1544716278-ca5e3f4abd8c", None),
      ("Leather Bookmark", "BOK-BMK-001", "Genuine leather handmade book marker", "5.99", "photo-1544716278-ca5e3f4abd8c", None)
    ]
  },
  {
    "category": "Health & Personal Care > Oral Care",
    "brand": "OralFresh",
    "items": [
      ("Bamboo Toothbrush 4-Pack", "HPC-BAMB-001", "Eco-friendly natural bamboo toothbrushes", "7.99", "photo-1607613009820-a29f7bb81c04", None),
      ("Charcoal Toothpaste", "HPC-PAST-001", "Natural activated charcoal teeth whitening paste", "6.49", "photo-1607613009820-a29f7bb81c04", None),
      ("Water Dental Flosser", "HPC-FLOS-001", "Cordless portable water flosser oral irrigator", "34.99", "photo-1607613009820-a29f7bb81c04", None)
    ]
  },
  {
    "category": "Health & Personal Care > Skin & Body",
    "brand": "PureGlow",
    "items": [
      ("Moisturizing Cream", "HPC-MOIST-001", "Deep hydrating facial moisturizing cream, 1.7 oz", "18.99", "photo-1608248597481-496100c8c836", None),
      ("Organic Lip Balm Set", "HPC-BALM-001", "Pack of 4 beeswax lip balm, assorted flavors", "7.49", "photo-1608248597481-496100c8c836", None),
      ("Mineral Sunscreen SPF 50", "HPC-SUN-001", "Broad spectrum zinc oxide mineral face sunscreen", "14.99", "photo-1598440947619-2c35fc9aa908", None)
    ]
  },
  {
    "category": "Apparel > Shoes",
    "brand": "StepFit",
    "items": [
      ("Lightweight Running Shoes", "SH-RUN-001", "Breathable mesh cushion athletic road shoes", "49.99", "photo-1542291026-7eec264c27ff", None),
      ("Canvas Slip-on Sneakers", "SH-SLIP-001", "Casual lightweight walk canvas shoes", "24.99", "photo-1549298916-b41d501d3772", None),
      ("Orthotic Gel Insoles", "SH-INSL-001", "Shoe insoles for high arch support & pain relief", "14.99", "photo-1549298916-b41d501d3772", None)
    ]
  },
  {
    "category": "Home & Kitchen > Bedding & Bath",
    "brand": "SoftSnooze",
    "items": [
      ("Sateen Sheet Set Queen", "BED-SHT-001", "100% organic cotton sateen 400-thread count sheets", "59.99", "photo-1522771739844-6a9f6d5f14af", None),
      ("Turkish Cotton Towels", "BTH-TWL-001", "Set of 2 luxury Turkish cotton bath towels, plush", "34.99", "photo-1553531384-cc64ac80f931", None),
      ("Silk Sleep Eye Mask", "BED-MSK-001", "Pure mulberry silk sleep mask, ultra-soft", "12.99", "photo-1583847268964-b28dc8f51f92", None)
    ]
  },
  {
    "category": "Groceries > Snacks > Dried Fruit & Seeds",
    "brand": "SunNaturals",
    "items": [
      ("Organic Chia Seeds", "CHIA-001", "Organic black chia seeds superfood, 12 oz", "5.49", "photo-1550583724-b2692b85b150", {
        "servingSize": "15g", "calories": 70, "totalFat": "4.5g", "saturatedFat": "0.5g", "sodium": "0mg", "totalCarbohydrates": "6g", "dietaryFiber": "5g", "sugars": "0g", "protein": "3g"
      }),
      ("Organic Dried Cranberries", "CRAN-001", "Sweetened organic dried cranberries, 8 oz", "3.99", "photo-1599599810769-bcde5a160d32", {
        "servingSize": "40g", "calories": 130, "totalFat": "0g", "saturatedFat": "0g", "sodium": "5mg", "totalCarbohydrates": "33g", "dietaryFiber": "2g", "sugars": "29g", "protein": "0g"
      })
    ]
  },
  {
    "category": "Electronics > Smart Home",
    "brand": "VoltPlus",
    "items": [
      ("Smart LED Light Strip", "SMT-LED-001", "16.4ft RGB LED light strip with app control", "19.99", "photo-1558002038-1055907df827", None),
      ("Smart Temperature Sensor", "SMT-TEMP-001", "Wireless indoor temperature & humidity monitor", "14.99", "photo-1558002038-1055907df827", None)
    ]
  },
  {
    "category": "Home & Kitchen > Storage & Organization",
    "brand": "DeskCraft",
    "items": [
      ("Plastic Drawer Divider", "DIV-DRW-001", "Set of 4 adjustable drawer dividers", "14.99", "photo-1598300042247-d088f8ab3a91", None),
      ("Hanging Closet Organizer", "ORG-HNG-001", "5-shelf hanging closet organizer with side pockets", "17.99", "photo-1598300042247-d088f8ab3a91", None)
    ]
  }
]

# Total items in extra list: 3+3+3+3+3+3+3+3+2+2+2 = 30 products.
# 69 + 30 = 99 products. Let's add 1 more to hit exactly 100 additional products.
extra_products_specs.append({
  "category": "Home & Kitchen > Bath Accessories",
  "brand": "SoftSnooze",
  "items": [
    ("Memory Foam Bath Mat", "BTH-MAT-001", "Soft absorbent memory foam bath rug, non-slip", "15.99", "photo-1553531384-cc64ac80f931", None)
  ]
})

# Let's generate the remaining items
for block in extra_products_specs:
  category = block["category"]
  brand_name = block["brand"]
  
  for name, sku, desc, price, photo_id, nutrition in block["items"]:
    gtin = str(gtin_base)
    mpn = f"{brand_name[:2].upper()}-{sku}"
    
    product = {
      "@type": "Product",
      "productID": sku,
      "name": name,
      "sku": sku,
      "image": unsplash_img(photo_id),
      "brand": {
        "@type": "Brand",
        "name": brand_name
      },
      "offers": {
        "price": price,
        "priceCurrency": "USD",
        "priceSpecification": None,
        "@type": "Offer",
        "availability": "https://schema.org/InStock",
        "itemCondition": "https://schema.org/NewCondition"
      },
      "aggregateRating": None,
      "url": f"https://example.com/{sku.lower()}",
      "description": desc,
      "gtin": gtin,
      "mpn": mpn,
      "category": category
    }
    
    if nutrition:
      product["nutrition"] = nutrition
    else:
      product["nutrition"] = None
      
    generated_products.append(product)
    gtin_base += 1
    mpn_counter += 1

# Let's combine the lists
all_products = existing_products + generated_products

# Verify length of additional products is exactly 100
print(f"Original products: {len(existing_products)}")
print(f"Generated products: {len(generated_products)}")
print(f"Total products: {len(all_products)}")

# Write to target file
output_path = Path("/Users/nemri/Downloads/ucp-agent-demo/business_agent/src/business_agent/data/products.json")
with output_path.open("w", encoding="utf-8") as f:
  json.dump(all_products, f, indent=2, ensure_ascii=False)

print("Products generated successfully!")
