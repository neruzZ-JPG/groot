import numpy as np

class COOSparseMatrix:
    def __init__(self, data, row_indices, col_indices, shape, dtype=float):
        self.data = np.array(data, dtype=dtype)
        self.row_indices = np.array(row_indices, dtype=int)
        self.col_indices = np.array(col_indices, dtype=int)
        self.shape = shape
        self.dtype = dtype

    def asformat(self, format):
        if format.lower() == 'csr':
            # 转换为CSR格式
            return self.to_csr()
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def to_csr(self):
        # 将 COO 转换为 CSR 格式
        row_ptr = np.zeros(self.shape[0] + 1, dtype=int)
        for row in self.row_indices:
            row_ptr[row + 1] += 1

        # 计算前缀和来得到每个行的起始位置
        row_ptr = np.cumsum(row_ptr)
        
        col_indices = np.zeros(len(self.data), dtype=int)
        data = np.zeros_like(self.data)
        for idx, (r, c, d) in enumerate(zip(self.row_indices, self.col_indices, self.data)):
            pos = row_ptr[r]
            col_indices[pos] = c
            data[pos] = d
            row_ptr[r] += 1
        
        # 修正 row_ptr 以消除重复的增加
        row_ptr[1:] -= 1
        np.cumsum(row_ptr, out=row_ptr)
        
        return CSRSparseMatrix(data, col_indices, row_ptr, self.shape, self.dtype)

    def __str__(self):
        # 创建一个密集表示的矩阵以打印
        dense_matrix = np.zeros(self.shape, dtype=self.dtype)
        np.fill_diagonal(dense_matrix, self.data[self.row_indices == self.col_indices])
        matrix_str = '\n'.join([' '.join([f'{val:8.4f}' for val in row]) for row in dense_matrix])
        return matrix_str

    def __mul__(self, other):
        # 矩阵乘法，目前只支持两个 COO 矩阵相乘
        if not isinstance(other, COOSparseMatrix):
            raise ValueError("The other matrix must be a COOSparseMatrix instance.")

        # 初始化结果矩阵的数据结构
        result_data = []
        result_row_indices = []
        result_col_indices = []

        # 遍历第一个矩阵的每一项
        for i, (d1, r1, c1) in enumerate(zip(self.data, self.row_indices, self.col_indices)):
            # 遍历第二个矩阵的每一项
            for j, (d2, r2, c2) in enumerate(zip(other.data, other.row_indices, other.col_indices)):
                if c1 == r2:  # 如果第一个矩阵的列索引匹配第二个矩阵的行索引
                    result_data.append(d1 * d2)
                    result_row_indices.append(r1)
                    result_col_indices.append(c2)

        # 转换结果到 COOSparseMatrix
        return COOSparseMatrix(
            np.array(result_data, dtype=self.dtype),
            np.array(result_row_indices, dtype=int),
            np.array(result_col_indices, dtype=int),
            (self.shape[0], other.shape[1])
        )

class CSRSparseMatrix:
    def __init__(self, data, col_indices, row_ptr, shape, dtype=float):
        self.data = np.array(data, dtype=dtype)
        self.col_indices = np.array(col_indices, dtype=int)
        self.row_ptr = np.array(row_ptr, dtype=int)
        self.shape = shape
        self.dtype = dtype

    def sum_axis(self, axis):
        if axis == 1:
            return np.array([np.sum(self.data[row_ptr[i]:row_ptr[i+1]]) for i in range(self.shape[0])])
        else:
            raise NotImplementedError("Summing over axis 0 is not implemented.")

    def __str__(self):
        coo = self.to_coo()
        return coo.__str__()


    def to_coo(self):
        # 将 CSR 矩阵转换为 COO 矩阵
        data = self.data
        row_ptr = self.row_ptr
        col_indices = self.col_indices

        # 初始化 COO 矩阵的索引和数据列表
        coo_row_indices = []
        coo_col_indices = []
        for row in range(self.shape[0]):
            row_start = row_ptr[row]
            row_end = row_ptr[row + 1]
            for idx in range(row_start, row_end):
                col = col_indices[idx]
                coo_row_indices.append(row)
                coo_col_indices.append(col)

        return COOSparseMatrix(
            np.array(data, dtype=self.dtype),
            np.array(coo_row_indices, dtype=int),
            np.array(coo_col_indices, dtype=int),
            self.shape
        )