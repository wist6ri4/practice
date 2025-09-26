import itertools

# ===============================
# 設定項目（ここを変更するだけで動作を変えられる）
# ===============================
CONFIG = {
    'NUM_COUNT': 3,              # 数字の個数（2以上）
    'NUMBER_RANGE': (1, 6),      # 使用する数字の範囲 (min, max)
    'TARGET_VALUE': 10,          # 目標値
    'USE_PARENTHESES': False,     # 括弧を使用するかどうか
    'OPERATORS': ['+', '-', '*', '/'],  # 使用する演算子
    'SHOW_FORMULAS': True,       # 結果の式を表示するかどうか
    'MAX_FORMULA_DISPLAY': 5     # 最大表示式数（0で全て表示）
}

def calculate(a, op, b):
    """安全な演算を実行"""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if abs(b) < 1e-9:
            raise ZeroDivisionError("Division by zero")
        return a / b
    else:
        raise ValueError(f"Unknown operator: {op}")

def evaluate_without_parentheses(nums, operators):
    """括弧なしで演算子の優先順位に従って評価"""
    temp_nums = list(nums)
    temp_ops = list(operators)

    # まず掛け算と割り算を処理
    i = 0
    while i < len(temp_ops):
        if temp_ops[i] in ['*', '/']:
            result = calculate(temp_nums[i], temp_ops[i], temp_nums[i+1])
            temp_nums[i] = result
            temp_nums.pop(i+1)
            temp_ops.pop(i)
        else:
            i += 1

    # 次に足し算と引き算を処理
    i = 0
    while i < len(temp_ops):
        result = calculate(temp_nums[i], temp_ops[i], temp_nums[i+1])
        temp_nums[i] = result
        temp_nums.pop(i+1)
        temp_ops.pop(i)

    return temp_nums[0]

def evaluate_with_parentheses_3nums(nums, ops):
    """3つの数字の場合の括弧パターンを評価"""
    a, b, c = nums
    op1, op2 = ops

    patterns = [
        # (a op1 b) op2 c
        lambda: calculate(calculate(a, op1, b), op2, c),
        # a op1 (b op2 c)
        lambda: calculate(a, op1, calculate(b, op2, c))
    ]

    pattern_formulas = [
        f"({a} {op1} {b}) {op2} {c}",
        f"{a} {op1} ({b} {op2} {c})"
    ]

    results = []
    for i, pattern_func in enumerate(patterns):
        try:
            result = pattern_func()
            results.append((result, pattern_formulas[i]))
        except (ZeroDivisionError, ValueError):
            continue

    return results

def evaluate_with_parentheses_4nums(nums, ops):
    """4つの数字の場合の括弧パターンを評価"""
    a, b, c, d = nums
    op1, op2, op3 = ops

    patterns = [
        # (a op1 b) op2 (c op3 d)
        lambda: calculate(calculate(a, op1, b), op2, calculate(c, op3, d)),
        # ((a op1 b) op2 c) op3 d
        lambda: calculate(calculate(calculate(a, op1, b), op2, c), op3, d),
        # a op1 ((b op2 c) op3 d)
        lambda: calculate(a, op1, calculate(calculate(b, op2, c), op3, d)),
        # a op1 (b op2 (c op3 d))
        lambda: calculate(a, op1, calculate(b, op2, calculate(c, op3, d))),
        # (a op1 (b op2 c)) op3 d
        lambda: calculate(calculate(a, op1, calculate(b, op2, c)), op3, d)
    ]

    pattern_formulas = [
        f"({a} {op1} {b}) {op2} ({c} {op3} {d})",
        f"(({a} {op1} {b}) {op2} {c}) {op3} {d}",
        f"{a} {op1} (({b} {op2} {c}) {op3} {d})",
        f"{a} {op1} ({b} {op2} ({c} {op3} {d}))",
        f"({a} {op1} ({b} {op2} {c})) {op3} {d}"
    ]

    results = []
    for i, pattern_func in enumerate(patterns):
        try:
            result = pattern_func()
            results.append((result, pattern_formulas[i]))
        except (ZeroDivisionError, ValueError):
            continue

    return results

def find_target_combinations():
    """設定に基づいて目標値になる組み合わせを検索"""
    count = 0
    formula_count = 0
    num_count = CONFIG['NUM_COUNT']
    min_num, max_num = CONFIG['NUMBER_RANGE']
    numbers = range(min_num, max_num + 1)
    operators = CONFIG['OPERATORS']
    target_value = CONFIG['TARGET_VALUE']
    use_parentheses = CONFIG['USE_PARENTHESES']

    print("設定:")
    print(f"  数字の個数: {num_count}")
    print(f"  数字の範囲: {min_num}～{max_num}")
    print(f"  目標値: {target_value}")
    print(f"  括弧使用: {'有効' if use_parentheses else '無効'}")
    print(f"  演算子: {operators}")
    print("-" * 50)

    # 数字の組み合わせを生成
    for nums_combo in itertools.product(numbers, repeat=num_count):
        found_target_in_this_combo = False

        # 演算子の組み合わせを生成
        for ops_combo in itertools.product(operators, repeat=num_count - 1):
            try:
                results_to_check = []

                # 括弧なしで評価
                result_no_paren = evaluate_without_parentheses(nums_combo, ops_combo)
                formula_parts = []
                for i in range(len(nums_combo)):
                    formula_parts.append(str(nums_combo[i]))
                    if i < len(ops_combo):
                        formula_parts.append(ops_combo[i])
                formula_no_paren = ' '.join(formula_parts)
                results_to_check.append((result_no_paren, formula_no_paren))

                # 括弧ありで評価（設定が有効な場合）
                if use_parentheses:
                    if num_count == 3:
                        paren_results = evaluate_with_parentheses_3nums(nums_combo, ops_combo)
                        results_to_check.extend(paren_results)
                    elif num_count == 4:
                        paren_results = evaluate_with_parentheses_4nums(nums_combo, ops_combo)
                        results_to_check.extend(paren_results)

                # 全ての結果をチェック
                for result, formula in results_to_check:
                    if abs(result - target_value) < 1e-9:
                        if CONFIG['SHOW_FORMULAS']:
                            if CONFIG['MAX_FORMULA_DISPLAY'] == 0 or formula_count < CONFIG['MAX_FORMULA_DISPLAY']:
                                print(f"式: {formula} = {target_value}")
                                formula_count += 1
                            elif formula_count == CONFIG['MAX_FORMULA_DISPLAY']:
                                print("（これ以上の式は省略...）")
                                formula_count += 1

                        found_target_in_this_combo = True
                        break

                if found_target_in_this_combo:
                    break

            except (ZeroDivisionError, ValueError):
                continue

        if found_target_in_this_combo:
            count += 1

    total_combinations = len(numbers) ** num_count
    return count, total_combinations

if __name__ == "__main__":
    found_count, total_count = find_target_combinations()
    probability = (found_count / total_count) * 100

    print("=" * 50)
    print(f"数字の組み合わせ総数: {total_count}")
    print(f"目標値になる組み合わせ数: {found_count}")
    print(f"確率: {probability:.2f}%")
