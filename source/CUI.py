import os
import sys
import msvcrt  # Windows用のキー入力取得

class VendingMachine:
    def __init__(self):
        # 商品情報を初期化（商品名、価格、販売数、売上）
        self.products = {
            1: {"name": "特製ラーメン", "price": 1000, "sales": 0, "revenue": 0},
            2: {"name": "醤油ラーメン", "price": 780, "sales": 0, "revenue": 0},
            3: {"name": "しおラーメン", "price": 880, "sales": 0, "revenue": 0},
            4: {"name": "ごはん", "price": 150, "sales": 0, "revenue": 0}
        }
        self.cart = {}  # 購入カート

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_title(self):
        self.clear_screen()
        print("***********************")
        print("\n 券売機シミュレータ\n")
        print("***********************")
        print("\nPlease Enter (Enterキー押下で画面がクリアされて処理が進む）")
        print("\n       （ESCキー押下で 管理画面に処理が進む）")
        print("\n       （qキー押下でシミュレータ終了）")

    def show_menu(self):
        print("\n商品      金額")
        print("=======================")
        for id, product in self.products.items():
            print(f"{id}.{product['name']} {product['price']}円")

    def process_purchase(self):
        self.cart = {}  # カートを初期化
        while True:
            print("\n———")
            choice = input("購入する商品番号(支払いに進む場合はc)>")
            
            if choice.lower() == 'c':
                break
            
            try:
                choice = int(choice)
                if choice in self.products:
                    if choice in self.cart:
                        self.cart[choice] += 1
                    else:
                        self.cart[choice] = 1
                else:
                    print("商品番号またはcを指定してください。")
            except ValueError:
                print("商品番号またはcを指定してください。")

        # カートの内容と合計金額を表示
        if self.cart:
            total = 0
            print("\n———")
            print("\n商品       数量")
            for product_id, quantity in self.cart.items():
                product = self.products[product_id]
                print(f"{product_id}.{product['name']}   {quantity}")
                total += product['price'] * quantity
            print("===")
            print(f"\n合計{total}円")
            print("———")

            # 支払い処理
            while True:
                try:
                    payment = int(input("\n現金を投入してください>"))
                    if payment <= 0:
                        print("正しい金額を入力してください。")
                        return False
                    if payment < total:
                        print("金額が不足しています。")
                        return False
                    
                    # おつりを計算
                    change = payment - total
                    print("———")
                    print(f"\nご購入ありがとうございます。おつり{change}円です。")
                    
                    # 売上を記録
                    for product_id, quantity in self.cart.items():
                        self.products[product_id]["sales"] += quantity
                        self.products[product_id]["revenue"] += self.products[product_id]["price"] * quantity
                    
                    return True
                except ValueError:
                    print("正しい金額を入力してください。")
                    return False

