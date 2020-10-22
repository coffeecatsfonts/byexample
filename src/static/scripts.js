function make_a_rowed_input_field() {
    rowed_input_field = "";
    
    for (i=0; i< 10; i++) {
        rowed_input_field += "    <input id=\"row_" + i + "\" name=\"row_" + i + "\" placeholder=\"" + i + "\" type=\"text\" class=\"first_ten_table_rows\">\n"
    }
    
    for (i=10; i< 95; i++) {
        rowed_input_field += "    <input id=\"row_" + i + "\" name=\"row_" + i + "\" placeholder=\"" + i + "\" type=\"text\" class=\"remaining_table_rows\">\n"
    }
    
    document.getElementById("rowed_input_field").innerHTML = rowed_input_field;
}
