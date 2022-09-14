for query_number in {0..35}
do
    echo "Query number: $query_number" 
    if [ ! -f ./image2labels/labels_$query_number.pkl ]; then
        nohup python make_annotations.py -q $query_number > ./logs/output_$query_number.log 2>&1 &
    fi
done