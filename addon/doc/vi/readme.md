# Khóa đầu vào #

* Tác giả: Jose Manuel Delicado
* NVDA compatibility: 2023.3.4 and beyond
* Tải về [phiên bản chính thức][1]

## Giới thiệu

Nhà bạn có trẻ em hay thú cưng không? Bạn có nuôi mèo, nó  leo trèo lên bàn
rất nhiều và đi lên cả bàn phím của bạn không? Có khi nào bạn di chuyển
chuột đến một vị trí ngoài ý muốn trên màn hình trong lúc dùng laptop không?
nếu có thì Input Lock (tạm dịch khóa bàn phím) là dành cho bạn! Bạn sẽ rời
khỏi máy tính của mình khi vẫn mở nó mà không xảy ra rủi ro nào.

Once installed, you will be able to lock your keyboard, touch screen (if
your laptop has one), touchpad, mouse and Braille display.

## Sử dụng

This addon adds three extra gestures to NVDA. By default they are
unassigned, so you will have to configure them from Input gestures
dialog. Read the NVDA User Guide for more information.

Khi bạn bấm thao tác bật / tắt khóa bàn phím, NVDA sẽ đọc "Input
locked". Các thiệt bị đầu vào của bạn sẽ bị khóa cho đến khi bạn bấm lại
thao tác đó. Trường hợp này, NVDA sẽ đọc "Input unlocked" và mọi thứ trở lại
hoạt động bình thường.

Locking the touchpad can prevent us from accidentally touching it,
especially those who are used to using the laptop keyboard directly. When
you press the toggle touchpad lock gesture, NVDA will say "Touchpad
locked". Your touchpad will be blocked until you press the same gesture
again. In that moment, NVDA will say "Touchpad unlocked" and everything will
work as usual.

Nếu bấm thao tác bật tắt chuột, chuột sẽ bị khóa. Bấm lại lệnh nữa để mở
khóa. Khi chuột bị khóa, bạn có thể dùng các thao tác của NVDA để di chuyển
và bấm chuột trái chuột phải, nhưng không thể di chuyển bằng chính con
chuột. Việc nhấp chuột cũng có thể vô hiệu hóa từ phân loại Input lock trong
hộp thoại cấu hình NVDA (NVDA 2018.2 trở lên) hoặc từ hộp thoại cài đặt
add-on cho các phiên bản cũ hơn, trong trình đơn tùy chọn. Thêm nữa, từ các
thiết lập này, bạn có thể chỉnh để khóa chuột khi khởi động NVDA.

Lưu ý: khi khóa nhấp chuột, bạn không thể dùng thao tác nào của NVDA với
chuột.

## Limitations and known problems

Input Lock has the following known problems:

* The shortcuts control+alt+del and windows+l can be used even when the
  keyboard is locked.
* For gestures used to lock the touchpad, please try to assign a small
  number of key combination gestures. It is recommended to use NVDA+letters
  or numbers, Ctrl+F keys etc.

## Bản ghi các thay đổi

### Version 1.13

* Now, minimum supported version is 2023.3.4.
* Updated translations. Starting from version 1.13, changelog won't be
  modified when a new release only includes localization updates.
* Added a gesture (unassigned by default) to lock/unlock the touchpad.

### Version 1.12

* Thêm tương thích cho các bản phát hành gần đây của NVDA.
* Cập nhật các bản phiên dịch.

### Version 1.11

* Thêm tương thích cho các bản phát hành gần đây của NVDA.
* Cập nhật các bản phiên dịch.
* Now, minimum supported version is 2022.4.

### Version 1.10

* Thêm tương thích cho các bản phát hành gần đây của NVDA.
* Cập nhật các bản phiên dịch.
* Updated documentation.
* Now, minimum supported version is 2021.3.
* The input will remain blocked after waking up from standby mode. Thanks to
  Javi Dominguez.

### Version 1.9

* Thêm tương thích cho các bản phát hành gần đây của NVDA.
* Cập nhật các bản phiên dịch.
* Updated documentation.

### Phiên bản 1.8

* Thêm tương thích cho các bản phát hành gần đây của NVDA.
* Cập nhật các bản phiên dịch.

### Phiên bản 1.7

* Thêm tương thích cho các bản phát hành gần đây của NVDA.
* Cập nhật các bản phiên dịch.

### Phiên bản 1.6

* Giờ đây, các thiết lập chỉ bị xóa bỏ khi gỡ cài đặt add-on. Cấu hình không
  còn bị khôi phục khi cài đặt cập nhật.
* Thêm mới và cập nhật các bản phiên dịch.

### Phiên bản 1.5

* Thêm tương thích cho các bản phát hành gần đây của NVDA.
* Các bản phiên dịch mới.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=inputLock
