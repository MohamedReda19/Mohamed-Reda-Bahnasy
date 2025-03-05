def selection_sort_ages(ages):
    # نسخة من القائمة الأصلية لتجنب التعديل المباشر
    sorted_ages = ages.copy()
    
    # طول القائمة
    n = len(sorted_ages)
    
    # تنفيذ Selection Sort
    for i in range(n):
        # افتراض أن العنصر الحالي هو الأصغر
        min_index = i
        
        # البحث عن العمر الأصغر في باقي القائمة
        for j in range(i+1, n):
            if sorted_ages[j] < sorted_ages[min_index]:
                min_index = j
        
        # تبديل العناصر
        sorted_ages[i], sorted_ages[min_index] = sorted_ages[min_index], sorted_ages[i]
    
    return sorted_ages

# مثال على استخدام الدالة
def main():
    # قائمة الأعمار
    students_ages = [22, 19, 25, 18, 20, 23, 21, 24]
    
    print("Original ages: ", students_ages)
    
    # الترتيب التصاعدي
    sorted_ages_asc = selection_sort_ages(students_ages)
    print("Ages in ascending order: ", sorted_ages_asc)
    
    # الترتيب التنازلي (عكس القائمة المرتبة)
    sorted_ages_desc = sorted_ages_asc[::-1]
    print("Ages in Descending order: ", sorted_ages_desc)
    
    # إحصائيات
    print("Oldest age: ", sorted_ages_asc[0])
    print("Youngest age: ", sorted_ages_asc[-1])
    print("Ages Avg: ", round(sum(students_ages) / len(students_ages), 2))

# تشغيل البرنامج
main()