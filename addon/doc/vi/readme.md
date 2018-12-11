# Input Lock #

* Tác giả: Jose Manuel Delicado
* Tải về [phiên bản chính thức][1]

## Giới thiệu

Nhà bạn có trẻ em hay thú cưng không? Bạn có nuôi mèo, nó  leo trèo lên bàn
rất nhiều và đi lên cả bàn phím của bạn không? Có khi nào bạn di chuyển
chuột đến một vị trí ngoài ý muốn trên màn hình trong lúc dùng laptop không?
nếu có thì Input Lock (tạm dịch khóa bàn phím) là dành cho bạn! Bạn sẽ rời
khỏi máy tính của mình khi vẫn mở nó mà không xảy ra rủi ro nào.

Khi đã cài đặt, bạn sẽ khóa được bàn phím, màn hình cảm ứng, chuột và màn
hình nổi nếu có.

## Sử dụng

Addon này gán thêm hai thao tác vào NVDA. Mặc định, chúng không được gán
phím tắt nên bạn phải cấu hình từ hộp thoại quản lý các thao tác. Đọc hướng
dẫn sử dụng NVDA để biết thêm thông tin.

Khi bạn bấm thao tác bật / tắt khóa bàn phím, NVDA sẽ đọc "Input
locked". Các thiệt bị đầu vào của bạn sẽ bị khóa cho đến khi bạn bấm lại
thao tác đó. Trường hợp này, NVDA sẽ đọc "Input unlocked" và mọi thứ trở lại
hoạt động bình thường.

Nếu bấm thao tác bật tắt chuột, chuột sẽ bị khóa. Bấm lại lệnh nữa để mở
khóa. Khi chuột bị khóa, bạn có thể dùng các thao tác của NVDA để di chuyển
và bấm chuột trái chuột phải, nhưng không thể di chuyển bằng chính con
chuột. Việc nhấp chuột cũng có thể vô hiệu hóa từ phân loại Input lock trong
hộp thoại cấu hình NVDA (NVDA 2018.2 trở lên) hoặc từ hộp thoại cài đặt
add-on cho các phiên bản cũ hơn, trong trình đơn tùy chọn. Thêm nữa, từ các
thiết lập này, bạn có thể chỉnh để khóa chuột khi khởi động NVDA.

Lưu ý: khi khóa nhấp chuột, bạn không thể dùng thao tác nào của NVDA với
chuột.

## Các giới hạn

Input Lock có các giới hạn sau đây:

* Phím tắt control+alt+del có thể dùng ngay cả khi khóa bàn phím.

## Bản ghi các thay đổi

### Phiên bản 1.4

* Mặc định, không gán thao tác cho add-on.

### Phiên bản 1.3

* Thêm bản cấu hình trong hộp thoại cấu hình NVDA. Với các phiên bản cũ,
  thêm một mục trên trình đơn và một hộp thoại.
* Thêm thiết lập để khóa chuột khi khởi động NVDA.
* Thêm thiết lập để khóa việc nhấp chuột khi chuột đã bị khóa.
* Sửa các lỗi nhỏ, vài cải thiện trong mã nguồn và gỡ bỏ các chuỗi văn bản
  trùng nhau cho người phiên dịch

### Phiên bản 1.2

* Giờ đây đã có thể khóa chuột
* Lệnh mới để chỉ khóa và mở khóa chuột

### Phiên bản 1.1

* Nếu một add-on khác trước đó đã thêm tính năng chụp vào quản lý đầu vào,
  nó sẽ được phục hồi khi mở khóa.

### Phiên bản 1.0

* Bản phát hành đầu tiên

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=inputlock