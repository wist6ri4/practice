// const isString = (str: string | number): str is string => {
//     return typeof str === 'string';
// }
// // 戻り値をbooleanにすると、型チェックの結果が引き継がれない
// // const isString = (str: string | number): boolean => {
// //     return typeof str === 'string';
// // }

// const add = (a: string | number, b: string | number): number => {
//     if(isString(a) || isString(b)) {
//         return Number(a) + Number(b);
//     } else {
//         return a + b; // 戻り値booleanだと、ここで型エラーになる
//     }
// }

// console.log(add(5, 10)); // 15
// console.log(add("5", "10")); // 15

const isString = (str: string | number): str is string => {
    return typeof str === 'string';
}

const add = (a: string | number, b: string | number): number => {
    if(isString(a) || isString(b)) {
        return Number(a) + Number(b);
    }
    return a + b;
}