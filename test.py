def process_cpu_data(metrics_list):
    """處理 CPU 的監控數據"""
    if not metrics_list:
        return 0.0
    
    filtered_data = []
    for data in metrics_list:
        # 篩選掉小於 0 或大於 100 的異常值
        if data >= 0 and data <= 100:
            filtered_data.append(data)
            
    if not filtered_data:
        return 0.0
        
    total_score = sum(filtered_data)
    data_count = len(filtered_data)
    final_average = total_score / data_count
    
    print(f"[LOG] CPU processing complete. Average: {final_average}")
    return round(final_average, 2)


def process_memory_data(metrics_list):
    """處理記憶體的監控數據"""
    if not metrics_list:
        return 0.0
    
    filtered_data = []
    for data in metrics_list:
        # 篩選掉小於 0 或大於 100 的異常值
        if data >= 0 and data <= 100:
            filtered_data.append(data)
            
    if not filtered_data:
        return 0.0
        
    total_score = sum(filtered_data)
    data_count = len(filtered_data)
    final_average = total_score / data_count
    
    print(f"[LOG] Memory processing complete. Average: {final_average}")
    return round(final_average, 2)