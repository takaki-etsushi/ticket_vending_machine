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
    def run(self):
            while True:
                self.show_title()
                try:
                    key = msvcrt.getch()  # キー入力を待機
                    
                    # ESCキー (27) が押された場合
                    if key == bytes([27]):
                        self.show_admin_menu()
                    # qキーが押された場合
                    elif key.lower() == b'q':
                        sys.exit()
                    # Enterキー (13) が押された場合
                    elif key == bytes([13]):
                        self.clear_screen()
                        self.show_menu()
                        self.process_purchase()
                        input("\nEnterキーを押してください...")
                except Exception as e:
                    print(f"エラーが発生しました: {e}")
                    break

    def show_admin_menu(self):
            self.clear_screen()
            print("***********************")
            print("\n       管理画面")
            print("\n***********************")
            self.show_sales_report()
            
            while True:
                print("\n=== 管理メニュー ====")
                print("\n1. 売上をリセットする")
                print("\n2. 商品の価格を変更する")
                print("\n3. 管理画面を終了する")
                print("\n———")
                
                choice = input("\n管理コード入力:")
                if choice == "1":
                    self.reset_sales()
                elif choice == "2":
                    self.change_price()
                elif choice == "3":
                    break

    def show_sales_report(self):
        print("\n======= 商品一覧 =======")
        print("\n商品      単価  販売数  売上金額")
        print("\n=======================")
        total_revenue = 0
        for id, product in self.products.items():
            revenue = product["revenue"]
            total_revenue += revenue
            print(f"{id}.{product['name']} {product['price']}円  {product['sales']}   {revenue:,}円")
        print("\n———")
        print(f"\n総売上金額 {total_revenue:,}円")

    def reset_sales(self):
        for product in self.products.values():
            product["sales"] = 0
            product["revenue"] = 0
        print("\n売上をリセットしました。")
        self.show_sales_report()
        
    def change_price(self):
        self.show_sales_report()
        
        try:
            product_id = int(input("\n価格を変更する商品の番号を入力してください。>"))
            if product_id not in self.products:
                print("無効な商品番号です。")
                return
            
            new_price = int(input("\n変更金額を入力してください。> "))
            if new_price <= 0:
                print("正しい金額を入力してください。")
                return
            
            print(f"\n【{product_id}.{self.products[product_id]['name']} {new_price}円】に変更します。")
            confirm = input("\nよろしいですか(Y/N）>")
            
            if confirm.lower() == 'y':
                self.products[product_id]["price"] = new_price
                print("\n変更しました。")
                self.show_sales_report()
            
        except ValueError:
            print("正しい値を入力してください。")

# メインプログラムの実行
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()