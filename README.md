# project-1
Dynamic Programming in NLP
Cài đặt các thuật toán Quy hoạch động để căn chỉnh chuỗi trong NLP:

LCS (Longest Common Subsequence) – ghép trùng tuyệt đối.

MinED (Minimum Edit Distance) – ghép gần đúng với chi phí chèn/xóa/thay.

LCS-based span alignment cho cross-tokenizer distillation (teacher ↔ student).

Mục tiêu: khi teacher và student dùng tokenizer khác nhau, cần đặt thẳng hàng hai dãy token trước khi gom phân phối (logits/embeddings) để distillation không mất ngữ nghĩa.
