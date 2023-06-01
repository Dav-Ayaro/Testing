#include <iostream>
#include <string>
#include <stack>

using namespace std;

double evaluate(string expression) {
  stack<double> nums;
  stack<char> ops;

  for (int i = 0; i < expression.length(); i++) {
    if (isdigit(expression[i])) {
      double num = 0;
      while (i < expression.length() && isdigit(expression[i])) {
        num = (num * 10) + (expression[i] - '0');
        i++;
      }
      i--;
      nums.push(num);
    } else if (expression[i] == '(') {
      ops.push(expression[i]);
    } else if (expression[i] == ')') {
      while (ops.top() != '(') {
        double num2 = nums.top();
        nums.pop();
        double num1 = nums.top();
        nums.pop();
        char op = ops.top();
        ops.pop();
        if (op == '+') {
          nums.push(num1 + num2);
        } else if (op == '-') {
          nums.push(num1 - num2);
        } else if (op == '*') {
          nums.push(num1 * num2);
        } else if (op == '/') {
          nums.push(num1 / num2);
        }
      }
      ops.pop();
    } else if (expression[i] == '+' || expression[i] == '-' ||
               expression[i] == '*' || expression[i] == '/') {
      while (!ops.empty() && ((expression[i] == '+' || expression[i] == '-') ||
                              (expression[i] == '*' || expression[i] == '/') &&
                              (ops.top() == '*' || ops.top() == '/'))) {
        double num2 = nums.top();
        nums.pop();
        double num1 = nums.top();
        nums.pop();
        char op = ops.top();
        ops.pop();
        if (op == '+') {
          nums.push(num1 + num2);
        } else if (op == '-') {
          nums.push(num1 - num2);
        } else if (op == '*') {
          nums.push(num1 * num2);
        } else if (op == '/') {
          nums.push(num1 / num2);
        }
      }
      ops.push(expression[i]);
    }
  }

  while (!ops.empty()) {
    double num2 = nums.top();
    nums.pop();
    double num1 = nums.top();
    nums.pop();
    char op = ops.top();
    ops.pop();
    if (op == '+') {
      nums.push(num1 + num2);
    } else if (op == '-') {
      nums.push(num1 - num2);
    } else if (op == '*') {
      nums.push(num1 * num2);
    } else if (op == '/') {
      nums.push(num1 / num2);
    }
  }

  return nums.top();
}

int main() {
  string expression;
  cout << "Enter a mathematical expression: ";
  cin >> expression;
  double result = evaluate(expression);
  cout << "Result: " << result << endl;
  return 0;
}
