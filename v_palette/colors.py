"""
    Colors info
"""

# fmt: off
MATERIAL = {
    "red":           {50:"#FFEBEE", 100:"#FFCDD2", 200:"#EF9A9A", 300:"#E57373", 400:"#EF5350", 500:"#F44336", 600:"#E53935", 700:"#D32F2F", 800:"#C62828", 900:"#B71C1C"}, # pylint: disable=line-too-long
    "pink":          {50:"#FCE4EC", 100:"#F8BBD0", 200:"#F48FB1", 300:"#F06292", 400:"#EC407A", 500:"#E91E63", 600:"#D81B60", 700:"#C2185B", 800:"#AD1457", 900:"#880E4F"}, # pylint: disable=line-too-long
    "purple":        {50:"#F3E5F5", 100:"#E1BEE7", 200:"#CE93D8", 300:"#BA68C8", 400:"#AB47BC", 500:"#9C27B0", 600:"#8E24AA", 700:"#7B1FA2", 800:"#6A1B9A", 900:"#4A148C"}, # pylint: disable=line-too-long
    "deep purple":   {50:"#EDE7F6", 100:"#D1C4E9", 200:"#B39DDB", 300:"#9575CD", 400:"#7E57C2", 500:"#673AB7", 600:"#5E35B1", 700:"#512DA8", 800:"#4527A0", 900:"#311B92"}, # pylint: disable=line-too-long
    "indigo":        {50:"#E8EAF6", 100:"#C5CAE9", 200:"#9FA8DA", 300:"#7986CB", 400:"#5C6BC0", 500:"#3F51B5", 600:"#3949AB", 700:"#303F9F", 800:"#283593", 900:"#1A237E"}, # pylint: disable=line-too-long
    "blue":          {50:"#E3F2FD", 100:"#BBDEFB", 200:"#90CAF9", 300:"#64B5F6", 400:"#42A5F5", 500:"#2196F3", 600:"#1E88E5", 700:"#1976D2", 800:"#1565C0", 900:"#0D47A1"}, # pylint: disable=line-too-long
    "light blue":    {50:"#E1F5FE", 100:"#B3E5FC", 200:"#81D4FA", 300:"#4FC3F7", 400:"#29B6F6", 500:"#03A9F4", 600:"#039BE5", 700:"#0288D1", 800:"#0277BD", 900:"#01579B"}, # pylint: disable=line-too-long
    "cyan":          {50:"#E0F7FA", 100:"#B2EBF2", 200:"#80DEEA", 300:"#4DD0E1", 400:"#26C6DA", 500:"#00BCD4", 600:"#00ACC1", 700:"#0097A7", 800:"#00838F", 900:"#006064"}, # pylint: disable=line-too-long
    "teal":          {50:"#E0F2F1", 100:"#B2DFDB", 200:"#80CBC4", 300:"#4DB6AC", 400:"#26A69A", 500:"#009688", 600:"#00897B", 700:"#00796B", 800:"#00695C", 900:"#004D40"}, # pylint: disable=line-too-long
    "green":         {50:"#E8F5E9", 100:"#C8E6C9", 200:"#A5D6A7", 300:"#81C784", 400:"#66BB6A", 500:"#4CAF50", 600:"#43A047", 700:"#388E3C", 800:"#2E7D32", 900:"#1B5E20"}, # pylint: disable=line-too-long
    "light green":   {50:"#F1F8E9", 100:"#DCEDC8", 200:"#C5E1A5", 300:"#AED581", 400:"#9CCC65", 500:"#8BC34A", 600:"#7CB342", 700:"#689F38", 800:"#558B2F", 900:"#33691E"}, # pylint: disable=line-too-long
    "lime":          {50:"#F9FBE7", 100:"#F0F4C3", 200:"#E6EE9C", 300:"#DCE775", 400:"#D4E157", 500:"#CDDC39", 600:"#C0CA33", 700:"#AFB42B", 800:"#9E9D24", 900:"#827717"}, # pylint: disable=line-too-long
    "yellow":        {50:"#FFFDE7", 100:"#FFF9C4", 200:"#FFF59D", 300:"#FFF176", 400:"#FFEE58", 500:"#FFEB3B", 600:"#FDD835", 700:"#FBC02D", 800:"#F9A825", 900:"#F57F17"}, # pylint: disable=line-too-long
    "amber":         {50:"#FFF8E1", 100:"#FFECB3", 200:"#FFE082", 300:"#FFD54F", 400:"#FFCA28", 500:"#FFC107", 600:"#FFB300", 700:"#FFA000", 800:"#FF8F00", 900:"#FF6F00"}, # pylint: disable=line-too-long
    "orange":        {50:"#FFF3E0", 100:"#FFE0B2", 200:"#FFCC80", 300:"#FFB74D", 400:"#FFA726", 500:"#FF9800", 600:"#FB8C00", 700:"#F57C00", 800:"#EF6C00", 900:"#E65100"}, # pylint: disable=line-too-long
    "deep orange":   {50:"#FBE9E7", 100:"#FFCCBC", 200:"#FFAB91", 300:"#FF8A65", 400:"#FF7043", 500:"#FF5722", 600:"#F4511E", 700:"#E64A19", 800:"#D84315", 900:"#BF360C"}, # pylint: disable=line-too-long
    "brown":         {50:"#EFEBE9", 100:"#D7CCC8", 200:"#BCAAA4", 300:"#A1887F", 400:"#8D6E63", 500:"#795548", 600:"#6D4C41", 700:"#5D4037", 800:"#4E342E", 900:"#3E2723"}, # pylint: disable=line-too-long
    "grey":          {50:"#FAFAFA", 100:"#F5F5F5", 200:"#EEEEEE", 300:"#E0E0E0", 400:"#BDBDBD", 500:"#9E9E9E", 600:"#757575", 700:"#616161", 800:"#424242", 900:"#212121"}, # pylint: disable=line-too-long
    "blue grey":     {50:"#ECEFF1", 100:"#CFD8DC", 200:"#B0BEC5", 300:"#90A4AE", 400:"#78909C", 500:"#607D8B", 600:"#546E7A", 700:"#455A64", 800:"#37474F", 900:"#263238"}, # pylint: disable=line-too-long
    "black":         {50:"#000000", 100:"#000000", 200:"#000000", 300:"#000000", 400:"#000000", 500:"#000000", 600:"#000000", 700:"#000000", 800:"#000000", 900:"#000000"}, # pylint: disable=line-too-long
    "white":         {50:"#FFFFFF", 100:"#FFFFFF", 200:"#FFFFFF", 300:"#FFFFFF", 400:"#FFFFFF", 500:"#FFFFFF", 600:"#FFFFFF", 700:"#FFFFFF", 800:"#FFFFFF", 900:"#FFFFFF"}  # pylint: disable=line-too-long
}

FLAT = {
    "turquoise":     {50:"#E8F8F5", 100:"#D1F2EB", 200:"#A3E4D7", 300:"#76D7C4", 400:"#48C9B0", 500:"#1ABC9C", 600:"#17A589", 700:"#148F77", 800:"#117864", 900:"#0E6251"}, # pylint: disable=line-too-long
    "green-sea":     {50:"#E8F6F3", 100:"#D0ECE7", 200:"#A2D9CE", 300:"#73C6B6", 400:"#45B39D", 500:"#16A085", 600:"#138D75", 700:"#117A65", 800:"#0E6655", 900:"#0B5345"}, # pylint: disable=line-too-long
    "emerald":       {50:"#EAFAF1", 100:"#D5F5E3", 200:"#ABEBC6", 300:"#82E0AA", 400:"#58D68D", 500:"#2ECC71", 600:"#28B463", 700:"#239B56", 800:"#1D8348", 900:"#186A3B"}, # pylint: disable=line-too-long
    "nephritis":     {50:"#E9F7EF", 100:"#D4EFDF", 200:"#A9DFBF", 300:"#7DCEA0", 400:"#52BE80", 500:"#27AE60", 600:"#229954", 700:"#1E8449", 800:"#196F3D", 900:"#145A32"}, # pylint: disable=line-too-long
    "peter-river":   {50:"#EBF5FB", 100:"#D6EAF8", 200:"#AED6F1", 300:"#85C1E9", 400:"#5DADE2", 500:"#3498DB", 600:"#2E86C1", 700:"#2874A6", 800:"#21618C", 900:"#1B4F72"}, # pylint: disable=line-too-long
    "belize-hole":   {50:"#EAF2F8", 100:"#D4E6F1", 200:"#A9CCE3", 300:"#7FB3D5", 400:"#5499C7", 500:"#2980B9", 600:"#2471A3", 700:"#1F618D", 800:"#1A5276", 900:"#154360"}, # pylint: disable=line-too-long
    "amethyst":      {50:"#F5EEF8", 100:"#EBDEF0", 200:"#D7BDE2", 300:"#C39BD3", 400:"#AF7AC5", 500:"#9B59B6", 600:"#884EA0", 700:"#76448A", 800:"#633974", 900:"#512E5F"}, # pylint: disable=line-too-long
    "wisteria":      {50:"#F4ECF7", 100:"#E8DAEF", 200:"#D2B4DE", 300:"#BB8FCE", 400:"#A569BD", 500:"#8E44AD", 600:"#7D3C98", 700:"#6C3483", 800:"#5B2C6F", 900:"#4A235A"}, # pylint: disable=line-too-long
    "wet-asphalt":   {50:"#EBEDEF", 100:"#D6DBDF", 200:"#AEB6BF", 300:"#85929E", 400:"#5D6D7E", 500:"#34495E", 600:"#2E4053", 700:"#283747", 800:"#212F3C", 900:"#1B2631"}, # pylint: disable=line-too-long
    "midnight-blue": {50:"#EAECEE", 100:"#D5D8DC", 200:"#ABB2B9", 300:"#808B96", 400:"#566573", 500:"#2C3E50", 600:"#273746", 700:"#212F3D", 800:"#1C2833", 900:"#17202A"}, # pylint: disable=line-too-long
    "sunflower":     {50:"#FEF9E7", 100:"#FCF3CF", 200:"#F9E79F", 300:"#F7DC6F", 400:"#F4D03F", 500:"#F1C40F", 600:"#D4AC0D", 700:"#B7950B", 800:"#9A7D0A", 900:"#7D6608"}, # pylint: disable=line-too-long
    "orange":        {50:"#FEF5E7", 100:"#FDEBD0", 200:"#FAD7A0", 300:"#F8C471", 400:"#F5B041", 500:"#F39C12", 600:"#D68910", 700:"#B9770E", 800:"#9C640C", 900:"#7E5109"}, # pylint: disable=line-too-long
    "carrot":        {50:"#FDF2E9", 100:"#FAE5D3", 200:"#F5CBA7", 300:"#F0B27A", 400:"#EB984E", 500:"#E67E22", 600:"#CA6F1E", 700:"#AF601A", 800:"#935116", 900:"#784212"}, # pylint: disable=line-too-long
    "pumpkin":       {50:"#FBEEE6", 100:"#F6DDCC", 200:"#EDBB99", 300:"#E59866", 400:"#DC7633", 500:"#D35400", 600:"#BA4A00", 700:"#A04000", 800:"#873600", 900:"#6E2C00"}, # pylint: disable=line-too-long
    "alizarin":      {50:"#FDEDEC", 100:"#FADBD8", 200:"#F5B7B1", 300:"#F1948A", 400:"#EC7063", 500:"#E74C3C", 600:"#CB4335", 700:"#B03A2E", 800:"#943126", 900:"#78281F"}, # pylint: disable=line-too-long
    "pomegranate":   {50:"#F9EBEA", 100:"#F2D7D5", 200:"#E6B0AA", 300:"#D98880", 400:"#CD6155", 500:"#C0392B", 600:"#A93226", 700:"#922B21", 800:"#7B241C", 900:"#641E16"}, # pylint: disable=line-too-long
    "clouds":        {50:"#FDFEFE", 100:"#FBFCFC", 200:"#F7F9F9", 300:"#F4F6F7", 400:"#F0F3F4", 500:"#ECF0F1", 600:"#D0D3D4", 700:"#B3B6B7", 800:"#979A9A", 900:"#7B7D7D"}, # pylint: disable=line-too-long
    "silver":        {50:"#F8F9F9", 100:"#F2F3F4", 200:"#E5E7E9", 300:"#D7DBDD", 400:"#CACFD2", 500:"#BDC3C7", 600:"#A6ACAF", 700:"#909497", 800:"#797D7F", 900:"#626567"}, # pylint: disable=line-too-long
    "concrete":      {50:"#F4F6F6", 100:"#EAEDED", 200:"#D5DBDB", 300:"#BFC9CA", 400:"#AAB7B8", 500:"#95A5A6", 600:"#839192", 700:"#717D7E", 800:"#5F6A6A", 900:"#4D5656"}, # pylint: disable=line-too-long
    "asbestos":      {50:"#F2F4F4", 100:"#E5E8E8", 200:"#CCD1D1", 300:"#B2BABB", 400:"#99A3A4", 500:"#7F8C8D", 600:"#707B7C", 700:"#616A6B", 800:"#515A5A", 900:"#424949"}  # pylint: disable=line-too-long
}
# fmt: on
