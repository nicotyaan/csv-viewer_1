import pandas as pd

def main():
    df = None  # 読み込んだデータを保持

    while True:
        print("\n=== CSV データ分析ツール ===")
        print("1. CSV を読み込む")
        print("2. 先頭 n 行を表示")
        print("3. 行数・列数を表示")
        print("4. 基本統計量を表示")
        print("5. 列名一覧を表示")
        print("6. 列でフィルタ")
        print("7. 列でソート")
        print("8. 終了")

        choice = input("番号を選んでください: ")

        if choice == "1":
            df = load_csv()
        elif choice == "2":
            show_head(df)
        elif choice == "3":
            show_shape(df)
        elif choice == "4":
            show_stats(df)
        elif choice == "5":
            show_columns(df)
        elif choice == "6":
            filter_column(df)
        elif choice == "7":
            sort_column(df)
        elif choice == "8":
            print("終了します。")
            break
        else:
            print("無効な入力です。")
            
def load_csv():
    filename = input("CSVファイル名を入力してください: ")
    try:
        df = pd.read_csv(filename)
        print("読み込み成功!")
        return df
    except Exception as e:
        print("読み込みエラー:", e)
        return None
    
def show_head(df):
    if df is None:
        print("先に CSV を読み込んでください。")
        return
    n = int(input("何行表示しますか？: "))
    print(df.head(n))
    
def show_shape(df):
    if df is None:
        print("先に CSV を読み込んでください。")
        return
    print(f"行数: {df.shape[0]}, 列数: {df.shape[1]}")
    
def show_stats(df):
    if df is None:
        print("先に CSV を読み込んでください。")
        return
    print(df.describe())
    
def show_columns(df):
    if df is None:
        print("先に CSV を読み込んでください。")
        return
    print("列名一覧:")
    for col in df.columns:
        print("-", col)
        
def filter_column(df):
    if df is None:
        print("先に CSV を読み込んでください。")
        return

    col = input("フィルタする列名を入力: ")
    if col not in df.columns:
        print("その列は存在しません。")
        return

    value = input("どの値でフィルタしますか？: ")

    filtered = df[df[col].astype(str) == value]
    print(filtered)
    
def sort_column(df):
    if df is None:
        print("先に CSV を読み込んでください。")
        return

    col = input("ソートする列名を入力: ")
    if col not in df.columns:
        print("その列は存在しません。")
        return

    order = input("昇順なら1、降順なら2: ")
    ascending = True if order == "1" else False

    sorted_df = df.sort_values(by=col, ascending=ascending)
    print(sorted_df)