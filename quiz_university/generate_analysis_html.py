# generate_analysis_html.py

# ==============================
# 🚩 Các template HTML phân tích chi tiết (dùng cho TAB PHÂN TÍCH CHI TIẾT)
# ==============================
ANALYSIS_HTMLS = {
    "social": """
        <h3>Phân Tích Chi Tiết: Xã hội – Nhân văn</h3>
        <p>Bạn có tố chất phù hợp với các ngành giáo dục, công tác xã hội, tâm lý, luật, văn học, truyền thông xã hội – những lĩnh vực cần sự kiên nhẫn, khả năng lắng nghe, kỹ năng giao tiếp và tinh thần hỗ trợ cộng đồng.</p>

        <h4>Kỹ năng mềm (Soft Skills):</h4>
        <p>Bộ câu hỏi đánh giá khả năng giao tiếp, làm việc nhóm, thuyết trình, quản lý thời gian, động viên nhóm, và lắng nghe người khác:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có khả năng giao tiếp tự tin, lắng nghe, dẫn dắt nhóm và xử lý mâu thuẫn – những kỹ năng quan trọng khi làm giáo viên, cố vấn, nhân viên xã hội, quản lý lớp học hoặc điều phối dự án cộng đồng.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn cần rèn luyện kỹ năng trình bày quan điểm rõ ràng, phản hồi tích cực khi làm việc nhóm, quản lý thời gian tốt hơn khi tham gia hoạt động.</li>
            <li><strong>Cách cải thiện:</strong>
                <ul>
                    <li>Tham gia câu lạc bộ, nhóm thảo luận, tình nguyện để thực hành giao tiếp.</li>
                    <li>Luyện tập phản hồi tích cực và kỹ năng lắng nghe qua các bài tập nhóm.</li>
                    <li>Ghi chú và đánh giá quá trình làm việc nhóm của mình để tự cải thiện.</li>
                </ul>
            </li>
        </ul>

        <h4>Kỹ năng chuyên môn (Professional Skills):</h4>
        <p>Bộ câu hỏi này giúp đánh giá mức độ lập kế hoạch học tập, nắm kiến thức chuyên ngành, tham gia nghiên cứu, phân tích vấn đề xã hội, tự đánh giá kết quả học tập, và ứng dụng công cụ hỗ trợ học tập:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có khả năng lập kế hoạch học tập rõ ràng, nắm vững kiến thức chuyên ngành, tham gia và chủ động trong các hoạt động ngoại khóa, hội thảo, thảo luận nhóm, và ứng dụng công cụ số hỗ trợ học tập.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn cần nâng cao tính chủ động trong học tập, cải thiện kỹ năng phân tích tình huống xã hội, tham gia các buổi hội thảo, workshop chuyên ngành, sử dụng công cụ số để ghi chú, lập kế hoạch.</li>
            <li><strong>Cách cải thiện:</strong>
                <ul>
                    <li>Tham gia các lớp học kỹ năng mềm và kỹ năng học tập hiệu quả.</li>
                    <li>Thực hiện nghiên cứu nhỏ liên quan ngành học và trình bày trước nhóm.</li>
                    <li>Sử dụng Notion, Obsidian hoặc Google Calendar để lập kế hoạch học tập.</li>
                    <li>Tham gia hội thảo chuyên đề hoặc các câu lạc bộ học thuật.</li>
                </ul>
            </li>
        </ul>

        <h4>Tư duy sáng tạo (Creative Thinking):</h4>
        <p>Bộ câu hỏi này phản ánh mức độ bạn đưa ra ý tưởng mới, cải tiến cách học, sáng tạo ví dụ minh họa, tạo nội dung học tập và sử dụng công cụ số để học tập sáng tạo:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có khả năng sáng tạo phương pháp học, tìm ví dụ minh họa dễ hiểu, giúp người khác hiểu kiến thức nhanh hơn, biết cách đổi mới phương pháp học tập, và áp dụng công cụ số hiệu quả.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn nên luyện tập cách biến kiến thức thành các ví dụ dễ hiểu, tạo sơ đồ tư duy, flashcard, chia sẻ kiến thức qua mạng xã hội, và thử áp dụng các phương pháp học khác nhau để tìm ra cách phù hợp nhất với bản thân.</li>
            <li><strong>Cách cải thiện:</strong>
                <ul>
                    <li>Tạo slide tóm tắt kiến thức và chia sẻ cho bạn bè.</li>
                    <li>Thử các công cụ như Canva, Mindmap để trực quan hóa kiến thức.</li>
                    <li>Luyện thuyết trình nội dung bạn đã học để tự kiểm tra sự hiểu biết.</li>
                    <li>Chia sẻ cách học của bạn qua các nhóm học tập hoặc mạng xã hội.</li>
                </ul>
            </li>
        </ul>

        <h4>Định hướng phát triển:</h4>
        <p>Để phát triển toàn diện trong ngành Xã hội – Nhân văn, bạn cần:</p>
        <ul>
            <li>Giữ vững tinh thần yêu con người, trách nhiệm cộng đồng, sẵn sàng hỗ trợ người khác.</li>
            <li>Kết hợp nâng cao kỹ năng mềm và chuyên môn, đồng thời sáng tạo trong cách học và chia sẻ kiến thức.</li>
            <li>Tham gia hoạt động tình nguyện, câu lạc bộ xã hội, dự án cộng đồng để rèn kỹ năng thực tế.</li>
            <li>Thiết lập mục tiêu cải thiện kỹ năng còn yếu trong 1–2 tháng và tự đánh giá sự tiến bộ của bản thân.</li>
        </ul>

        <p><strong>Lời khuyên:</strong> Hãy bắt đầu bằng những hành động nhỏ như tham gia một buổi workshop, đọc thêm sách liên quan ngành, luyện thuyết trình, chia sẻ bài học với người khác. Những thói quen này sẽ giúp bạn trở thành một người học chủ động và phát triển vững chắc trong lĩnh vực Xã hội – Nhân văn.</p>
    """,

    "tech": """
        <h3>Phân Tích Chi Tiết: Công nghệ – Kỹ thuật</h3>
        <p>Bạn có tiềm năng phát triển trong các ngành Khoa học máy tính, Kỹ thuật phần mềm, Kỹ thuật điện – điện tử, Cơ điện tử, Tự động hóa, và các lĩnh vực kỹ thuật ứng dụng khác. Nhóm ngành này yêu cầu sự tư duy logic, khả năng giải quyết vấn đề, tính kỷ luật và kỹ năng làm việc độc lập lẫn nhóm hiệu quả.</p>

        <h4>Kỹ năng mềm (Soft Skills):</h4>
        <p>Bộ câu hỏi đánh giá khả năng giao tiếp, làm việc nhóm kỹ thuật, trình bày giải pháp, tổ chức thời gian và hỗ trợ đồng đội trong quá trình làm dự án:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có kỹ năng phối hợp nhóm, trình bày giải pháp rõ ràng, chủ động giúp đỡ thành viên khác – rất quan trọng khi làm việc nhóm kỹ thuật, phát triển phần mềm hoặc lắp ráp hệ thống.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn cần nâng cao khả năng giao tiếp, phản hồi kỹ thuật, và rèn luyện tinh thần hợp tác khi làm nhóm.</li>
            <li><strong>Cách cải thiện:</strong>
                <ul>
                    <li>Tham gia các dự án lập trình hoặc chế tạo theo nhóm.</li>
                    <li>Giao tiếp kỹ thuật rõ ràng qua sơ đồ, tài liệu hoặc thuyết trình ngắn.</li>
                    <li>Rèn luyện quản lý thời gian bằng cách lập kế hoạch rõ ràng và theo dõi tiến độ.</li>
                </ul>
            </li>
        </ul>

        <h4>Kỹ năng chuyên môn (Technical Skills):</h4>
        <p>Phản ánh mức độ hiểu và ứng dụng kiến thức chuyên ngành như lập trình, đọc hiểu tài liệu kỹ thuật, vận hành thiết bị, sử dụng phần mềm kỹ thuật:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có nền tảng kỹ thuật tốt, khả năng áp dụng kiến thức vào thực tế như mô phỏng, thiết kế, hoặc lập trình – rất phù hợp cho các công việc kỹ thuật ứng dụng.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn cần củng cố kiến thức nền tảng (như toán – lý – tin), thực hành phần mềm chuyên ngành hoặc nâng cao kỹ năng đọc hiểu tài liệu kỹ thuật tiếng Anh.</li>
            <li><strong>Cách cải thiện:</strong>
                <ul>
                    <li>Luyện tập các bài tập kỹ thuật cơ bản (như lập trình thuật toán, mô phỏng mạch, vẽ 3D…).</li>
                    <li>Tham gia cuộc thi chuyên môn như hackathon, chế tạo robot hoặc dự án IoT nhỏ.</li>
                    <li>Dùng công cụ như GitHub, TinkerCAD, AutoCAD, Arduino IDE… để rèn kỹ năng thực hành.</li>
                </ul>
            </li>
        </ul>

        <h4>Tư duy sáng tạo (Creative Thinking):</h4>
        <p>Bộ câu hỏi đánh giá khả năng đổi mới giải pháp, tìm cách tối ưu hệ thống, đề xuất ý tưởng kỹ thuật hoặc sáng tạo ứng dụng mới:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có khả năng phát hiện vấn đề kỹ thuật, đề xuất giải pháp cải tiến hoặc tạo sản phẩm mới – đây là lợi thế lớn khi tham gia nghiên cứu và phát triển sản phẩm (R&D).</li>
            <li><strong>Điểm chưa cao:</strong> Bạn cần rèn luyện khả năng phân tích vấn đề đa chiều, dám thử nghiệm ý tưởng mới và học hỏi từ các sản phẩm có sẵn.</li>
            <li><strong>Cách cải thiện:</strong>
                <ul>
                    <li>Tham khảo các sản phẩm mở nguồn (open source), nghiên cứu cách người khác giải quyết vấn đề kỹ thuật.</li>
                    <li>Tham gia workshop sáng tạo sản phẩm kỹ thuật (Arduino, Raspberry Pi, AI mini project…)</li>
                    <li>Viết blog hoặc nhật ký kỹ thuật để rèn luyện tư duy cải tiến và phản biện kỹ thuật.</li>
                </ul>
            </li>
        </ul>

        <h4>🎯 Định hướng phát triển:</h4>
        <ul>
            <li>Giữ tinh thần học hỏi, thử nghiệm và cải tiến sản phẩm liên tục.</li>
            <li>Kết hợp kiến thức chuyên môn và kỹ năng mềm để làm việc hiệu quả trong nhóm kỹ thuật.</li>
            <li>Tạo sản phẩm nhỏ định kỳ (ví dụ: app, mô hình, robot mini…) để xây dựng portfolio cá nhân.</li>
            <li>Tham gia cộng đồng kỹ thuật online để học hỏi và cập nhật xu hướng mới.</li>
        </ul>

        <p><strong>Lời khuyên:</strong> Bắt đầu với một dự án cá nhân nhỏ, lập kế hoạch học tập rõ ràng, và giữ nhịp luyện tập kỹ năng hàng tuần. Kiên trì là chìa khóa trong ngành Công nghệ – Kỹ thuật.</p>

    """,

    "arts": """
        <h3>Phân Tích Chi Tiết: Nghệ thuật – Sáng tạo</h3>
        <p>Bạn có năng khiếu hoặc đam mê với các lĩnh vực thiết kế đồ họa, mỹ thuật, thời trang, sân khấu – điện ảnh, truyền thông thị giác, kiến trúc nội thất, hoặc các ngành sáng tạo nội dung. Những lĩnh vực này đề cao cảm xúc thẩm mỹ, khả năng biểu đạt cá nhân và sự linh hoạt trong tư duy sáng tạo.</p>

        <h4>Kỹ năng mềm (Soft Skills):</h4>
        <p>Bộ câu hỏi đánh giá khả năng giao tiếp, trình bày ý tưởng, làm việc nhóm sáng tạo, phản hồi nghệ thuật, và hỗ trợ đồng đội trong dự án:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có khả năng làm việc nhóm hiệu quả, trình bày ý tưởng rõ ràng và linh hoạt trong giao tiếp nghệ thuật – đây là nền tảng quan trọng khi làm việc với khách hàng, cộng sự hoặc trong các dự án nhóm sáng tạo.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn có thể gặp khó khăn khi thuyết trình sản phẩm, trao đổi quan điểm thiết kế hoặc kết nối với đồng nghiệp trong môi trường nghệ thuật đòi hỏi cởi mở và linh hoạt.</li>
            <li><strong>Cách cải thiện:</strong>
                <ul>
                    <li>Tham gia các buổi workshop, triển lãm, hoặc sự kiện nghệ thuật để học cách lắng nghe và trình bày ý tưởng.</li>
                    <li>Thực hành thuyết trình ngắn về sản phẩm của mình với bạn bè hoặc nhóm.</li>
                    <li>Giao tiếp đa phương tiện: dùng moodboard, sketch, hoặc slide để biểu đạt ý tưởng hiệu quả hơn.</li>
                </ul>
            </li>
        </ul>

        <h4>Kỹ năng chuyên môn (Technical/Professional Skills):</h4>
        <p>Phản ánh mức độ nắm vững kiến thức chuyên ngành, kỹ năng sử dụng phần mềm sáng tạo, hoàn thiện sản phẩm, và khả năng áp dụng kỹ thuật thẩm mỹ vào thực tế:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có kỹ năng sử dụng phần mềm tốt, khả năng hoàn thiện sản phẩm thẩm mỹ cao, và chủ động học hỏi xu hướng nghệ thuật mới – đây là những yếu tố then chốt trong môi trường sáng tạo cạnh tranh.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn cần củng cố kỹ năng chỉnh sửa, sử dụng phần mềm thiết kế, hoặc chưa thực sự làm quen với quy trình hoàn thiện sản phẩm nghệ thuật chuyên nghiệp.</li>
            <li><strong>Cách cải thiện:</strong>
                <ul>
                    <li>Học thêm các phần mềm chuyên ngành như Adobe Illustrator, Photoshop, Premiere, Blender, v.v.</li>
                    <li>Chọn dự án nhỏ có tính ứng dụng để luyện tập kỹ năng hoàn thiện và tinh chỉnh sản phẩm.</li>
                    <li>Tham khảo portfolio của người đi trước để hiểu tiêu chuẩn chất lượng sản phẩm nghệ thuật chuyên nghiệp.</li>
                </ul>
            </li>
        </ul>

        <h4>Tư duy sáng tạo (Creative Thinking):</h4>
        <p>Đánh giá khả năng đưa ra ý tưởng mới, thay đổi cách tiếp cận nghệ thuật, quan sát xu hướng thị trường và thể hiện bản sắc cá nhân qua sản phẩm:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có tư duy linh hoạt, dám thử nghiệm phong cách mới, đề xuất ý tưởng độc đáo, kết hợp yếu tố cá nhân và thị trường – đây là thế mạnh nổi bật trong lĩnh vực nghệ thuật đòi hỏi đổi mới liên tục.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn có thể đang ở giai đoạn “bắt chước” hoặc chưa tự tin thể hiện bản sắc cá nhân. Thiếu cảm hứng sáng tạo hoặc chưa biết cách phát triển ý tưởng thành sản phẩm hoàn chỉnh.</li>
            <li><strong>Cách cải thiện:</strong>
                <ul>
                    <li>Tạo thói quen quan sát sản phẩm sáng tạo của người khác (Behance, Pinterest, Instagram…).</li>
                    <li>Thử nghiệm phong cách khác nhau, hoặc kết hợp nhiều yếu tố để tạo “chất riêng”.</li>
                    <li>Ghi chú ý tưởng sáng tạo mỗi ngày, lập sổ tay ý tưởng hoặc bản moodboard cá nhân.</li>
                </ul>
            </li>
        </ul>

        <h4>🎯 Định hướng phát triển:</h4>
        <ul>
            <li>Tập trung xây dựng portfolio cá nhân đa dạng – đây là “tấm vé” nghề nghiệp quan trọng với người làm nghệ thuật.</li>
            <li>Kết hợp cảm xúc nghệ thuật và kỹ thuật trình bày sản phẩm chuyên nghiệp.</li>
            <li>Tham gia cộng đồng sáng tạo, cuộc thi nghệ thuật, triển lãm hoặc các nhóm sáng tác.</li>
            <li>Đặt mục tiêu cá nhân về số lượng sản phẩm/tháng để duy trì nhịp sáng tạo liên tục.</li>
        </ul>

        <p><strong>Lời khuyên:</strong> Sáng tạo không đến từ cảm hứng nhất thời – hãy tạo thói quen quan sát, luyện tập, và thể hiện bản thân thông qua mỗi sản phẩm. Hãy để tác phẩm nói lên “chất riêng” của bạn.</p>

    """,
    "health": """
        <h3>Phân Tích Chi Tiết: Y tế – Sức khỏe</h3>
        <p>Bạn có thiên hướng quan tâm tới sức khỏe con người, chăm sóc cộng đồng, hỗ trợ người bệnh và làm việc trong môi trường đòi hỏi sự kiên nhẫn, tỉ mỉ và tinh thần trách nhiệm cao. Nhóm ngành này bao gồm các lĩnh vực như điều dưỡng, y đa khoa, dược, kỹ thuật xét nghiệm, y tế công cộng và tâm lý học lâm sàng.</p>

        <h4>Kỹ năng mềm (Soft Skills):</h4>
        <p>Phản ánh khả năng làm việc nhóm trong môi trường trực ca, giao tiếp với bệnh nhân, lắng nghe, đồng cảm và ứng xử linh hoạt trong các tình huống y khoa:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có kỹ năng giao tiếp rõ ràng, khả năng làm việc nhóm tốt trong môi trường căng thẳng, biết quan tâm và lắng nghe người khác – đây là yếu tố quan trọng trong công việc chăm sóc và hỗ trợ sức khỏe bệnh nhân.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn có thể gặp khó khăn khi làm việc ca trực, xử lý tình huống căng thẳng, hoặc chưa tự tin khi tương tác với người bệnh hoặc đồng nghiệp.</li>
            <li><strong>Cách cải thiện:</strong>
                <ul>
                    <li>Tham gia các hoạt động cộng đồng, chiến dịch y tế để luyện sự đồng cảm và khả năng giao tiếp thực tế.</li>
                    <li>Thực hành thuyết trình ngắn hoặc chia sẻ tình huống trong nhóm học để nâng cao phản xạ giao tiếp.</li>
                    <li>Luyện kỹ năng quản lý thời gian và phản hồi trong nhóm để làm quen với mô hình làm việc y khoa.</li>
                </ul>
            </li>
        </ul>

        <h4>Kỹ năng chuyên môn (Professional/Technical Skills):</h4>
        <p>Đánh giá khả năng lập kế hoạch trực ca, nắm kiến thức y học, sử dụng công cụ y tế và phần mềm tra cứu, kỹ năng xử lý ca bệnh và ghi hồ sơ bệnh án:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có kiến thức y khoa tốt, sử dụng công cụ tra cứu thành thạo, thực hành lâm sàng linh hoạt, biết kết hợp phản xạ chuyên môn và giao tiếp khi xử lý ca bệnh.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn còn thiếu thực hành lâm sàng hoặc chưa tự tin khi sử dụng công cụ tra cứu, lập kế hoạch học tập, hoặc chưa có thói quen cập nhật tài liệu chuyên ngành.</li>
            <li><strong>Cách cải thiện:</strong>
                <ul>
                    <li>Tham gia thực tập, các buổi mô phỏng lâm sàng, hoặc lớp kỹ năng lâm sàng cơ bản.</li>
                    <li>Sử dụng phần mềm y học như Medscape, UpToDate để luyện tra cứu thường xuyên.</li>
                    <li>Học cách ghi chép hồ sơ bệnh án rõ ràng, đầy đủ – kỹ năng quan trọng trong môi trường thực tế.</li>
                </ul>
            </li>
        </ul>

        <h4>Tư duy sáng tạo (Creative Thinking):</h4>
        <p>Đo lường mức độ chủ động tìm cách tối ưu hóa quy trình chăm sóc, đề xuất cải tiến trong công việc, vận dụng công nghệ vào học tập và thực hành:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có khả năng quan sát vấn đề trong môi trường y tế và chủ động đưa ra giải pháp cải tiến quy trình, sáng tạo nội dung truyền thông y tế hoặc áp dụng công nghệ để hỗ trợ học tập hiệu quả.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn chưa quen với việc phản biện quy trình, chưa chủ động đưa ra sáng kiến mới hoặc còn ngại thử nghiệm các công cụ công nghệ để hỗ trợ công việc.</li>
            <li><strong>Cách cải thiện:</strong>
                <ul>
                    <li>Tham gia các cuộc thi sáng kiến chăm sóc sức khỏe cộng đồng, chiến dịch truyền thông y tế.</li>
                    <li>Học sử dụng các app học tập y khoa hoặc hệ thống mô phỏng lâm sàng để mở rộng tư duy.</li>
                    <li>Ghi nhận và cải tiến những bước nhỏ trong thao tác hằng ngày để hình thành tư duy đổi mới.</li>
                </ul>
            </li>
        </ul>

        <h4>Định hướng phát triển:</h4>
        <ul>
            <li>Xây dựng thói quen giao tiếp chuyên nghiệp, từ tốn, biết lắng nghe và đặt câu hỏi đúng lúc.</li>
            <li>Thường xuyên cập nhật kiến thức chuyên môn, tham gia lớp tập huấn kỹ năng lâm sàng.</li>
            <li>Tham gia hoạt động tình nguyện y tế để trau dồi kỹ năng thực tế và trách nhiệm cộng đồng.</li>
            <li>Dành thời gian tự đánh giá hiệu quả xử lý tình huống thực tế để học từ trải nghiệm.</li>
        </ul>

        <p><strong>Lời khuyên:</strong> Nghề y không chỉ cần kiến thức mà còn đòi hỏi tâm huyết, sự kiên nhẫn và tinh thần phục vụ. Hãy học cách giữ bình tĩnh, quan sát và không ngừng nâng cao kỹ năng để trở thành
    """,

    "social": """
        <h3>Phân Tích Chi Tiết: Xã hội – Nhân văn</h3>
        <p>Bạn phù hợp với lĩnh vực giáo dục, công tác xã hội, tâm lý, luật, văn học, truyền thông xã hội – những lĩnh vực cần sự kiên nhẫn, khả năng lắng nghe, kỹ năng giao tiếp và tinh thần hỗ trợ cộng đồng.</p>

        <h4>Kỹ năng mềm (Soft Skills):</h4>
        <p>Phản ánh khả năng giao tiếp, thuyết trình, làm việc nhóm, lắng nghe, giải quyết mâu thuẫn, và tổ chức thời gian:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn có khả năng tương tác tốt với người khác, dễ đồng cảm, trình bày rõ ràng quan điểm, linh hoạt xử lý tình huống xã hội. Những kỹ năng này rất cần trong giảng dạy, tư vấn, tổ chức sự kiện, hoặc điều phối hoạt động cộng đồng.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn cần luyện tập thêm khả năng trình bày, lắng nghe tích cực và phản hồi trong môi trường nhóm, cũng như cách kiểm soát thời gian trong các hoạt động cộng đồng.</li>
            <li><strong>Gợi ý cải thiện:</strong>
                <ul>
                    <li>Tham gia các nhóm thảo luận, CLB kỹ năng mềm hoặc hoạt động thiện nguyện để luyện thực tế.</li>
                    <li>Tập viết và chia sẻ quan điểm cá nhân qua blog, mạng xã hội, hoặc diễn đàn sinh viên.</li>
                    <li>Rèn thói quen đánh giá sau mỗi lần làm việc nhóm để cải thiện bản thân.</li>
                </ul>
            </li>
        </ul>

        <h4>Kỹ năng chuyên môn (Chuyên ngành):</h4>
        <p>Đánh giá khả năng lập kế hoạch học tập, hiểu kiến thức xã hội – nhân văn, phân tích tình huống, và vận dụng công cụ học tập:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn chủ động trong học tập, biết cách tổ chức thông tin, lập luận và liên hệ với thực tiễn. Bạn có thể theo đuổi các ngành cần tư duy phản biện như truyền thông, luật học, giáo dục công dân hoặc chính sách xã hội.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn có thể còn học theo kiểu ghi nhớ, thiếu ứng dụng hoặc ít tham gia hoạt động học thuật nâng cao.</li>
            <li><strong>Gợi ý cải thiện:</strong>
                <ul>
                    <li>Tham gia hội thảo, đọc sách phân tích tình huống xã hội, viết tiểu luận hoặc phân tích phim, truyện.</li>
                    <li>Ứng dụng các công cụ như Notion, Zotero, Obsidian để tổng hợp và phân tích tài liệu học tập.</li>
                    <li>Luyện phản biện bằng cách tự đưa ra nhận định về các vấn đề xã hội đang diễn ra.</li>
                </ul>
            </li>
        </ul>

        <h4>Tư duy sáng tạo:</h4>
        <p>Đánh giá khả năng đưa ra ý tưởng mới, ứng dụng phương pháp học đa dạng, và truyền cảm hứng cho cộng đồng học tập:</p>
        <ul>
            <li><strong>Điểm cao:</strong> Bạn biết cách làm mới cách học – như dùng sơ đồ tư duy, kể chuyện, ví dụ minh họa – rất phù hợp với vai trò người hướng dẫn, diễn giả, giáo viên, người làm nội dung giáo dục.</li>
            <li><strong>Điểm chưa cao:</strong> Bạn có thể còn phụ thuộc vào sách giáo khoa, chưa linh hoạt biến kiến thức thành sản phẩm sáng tạo.</li>
            <li><strong>Gợi ý cải thiện:</strong>
                <ul>
                    <li>Thiết kế infographics, flashcard, hoặc bài giảng mini để truyền đạt ý tưởng.</li>
                    <li>Chia sẻ kiến thức qua YouTube, podcast hoặc các bài đăng phân tích xã hội.</li>
                    <li>Tham gia các cuộc thi như hùng biện, viết luận, sáng tạo nội dung nhân văn.</li>
                </ul>
            </li>
        </ul>

        <h4>Định hướng phát triển:</h4>
        <ul>
            <li>Kết hợp kỹ năng mềm, tư duy phản biện và óc sáng tạo để tạo ra giá trị xã hội.</li>
            <li>Tìm kiếm cơ hội thực hành qua công việc tình nguyện, thực tập ngành giáo dục, tâm lý, công tác xã hội hoặc truyền thông.</li>
            <li>Đặt mục tiêu phát triển từng kỹ năng trong 1–2 tháng với sự tự đánh giá tiến bộ thường xuyên.</li>
        </ul>

        <p><strong>Lời khuyên:</strong> Nhóm ngành Xã hội – Nhân văn rất cần người biết truyền cảm hứng, thấu hiểu con người, và cam kết với cộng đồng. Dù bạn bắt đầu từ điểm nào, hãy kiên trì rèn luyện từng bước – từ việc chia sẻ một câu chuyện ý nghĩa đến chủ động hỗ trợ người khác trong nhóm. Đó là hành trình xây nền vững chắc cho người làm nhân văn thực thụ.</p>

    """,
    "science": """
    <h3>Phân Tích Chi Tiết: Nhóm ngành Khoa học – Tự nhiên</h3>
    <p>Bạn thuộc nhóm người có khả năng suy luận logic, yêu thích sự khám phá, phân tích và có xu hướng tìm hiểu bản chất sâu xa của các hiện tượng. Nhóm ngành Khoa học – Tự nhiên bao gồm: Toán học, Vật lý, Hóa học, Sinh học, Thiên văn học, Khoa học dữ liệu, Môi trường, Công nghệ sinh học, Khoa học vật liệu, và nhiều lĩnh vực nghiên cứu liên ngành.</p>

    <h4>Kỹ năng mềm (Soft Skills):</h4>
    <ul>
        <li><strong>Điểm cao:</strong> Bạn có khả năng giao tiếp học thuật, hợp tác nhóm khoa học tốt, có thể trình bày lập luận chặt chẽ và truyền đạt ý tưởng rõ ràng. Điều này đặc biệt phù hợp trong môi trường học thuật, thuyết trình nghiên cứu hoặc làm việc trong nhóm nghiên cứu liên ngành.</li>
        <li><strong>Điểm chưa cao:</strong> Có thể bạn còn e ngại khi trình bày ý tưởng, thiếu kỹ năng phản biện hoặc gặp khó khăn khi hợp tác nhóm giải quyết vấn đề.</li>
        <li><strong>Gợi ý cải thiện:</strong>
            <ul>
                <li>Tham gia các buổi seminar học thuật, câu lạc bộ tranh biện khoa học hoặc nhóm học tập.</li>
                <li>Luyện kỹ năng viết báo cáo và trình bày dự án khoa học bằng infographic, sơ đồ tư duy.</li>
                <li>Thực hành phản biện qua việc phân tích các lập luận trong bài báo khoa học hoặc tin tức khoa học đại chúng.</li>
                <li>Viết “Khoa học cho mọi người” – chuyển một chủ đề phức tạp thành ngôn ngữ đơn giản.</li>
            </ul>
        </li>
    </ul>

    <h4>Kỹ năng chuyên môn (Academic/Technical Skills):</h4>
    <ul>
        <li><strong>Điểm cao:</strong> Bạn có nền tảng kiến thức vững, có thể áp dụng công thức, mô hình, phân tích dữ liệu và sử dụng công cụ học tập hiện đại như phần mềm mô phỏng, lập trình phân tích.</li>
        <li><strong>Điểm chưa cao:</strong> Có thể bạn còn gặp khó khăn trong việc kết nối lý thuyết với thực hành, giải quyết tình huống thực tế hoặc chưa quen sử dụng công cụ kỹ thuật số để học tập.</li>
        <li><strong>Gợi ý phát triển:</strong>
            <ul>
                <li>Học sử dụng phần mềm chuyên ngành như: Python (khoa học dữ liệu), MATLAB (mô phỏng), Excel nâng cao (thống kê), GeoGebra (Toán học), Stellarium (Thiên văn), R hoặc SPSS (phân tích dữ liệu).</li>
                <li>Tham gia các khóa học online miễn phí (Coursera, edX, FutureLearn) về chuyên ngành khoa học.</li>
                <li>Làm project nhỏ: mô phỏng chuyển động vật lý, tạo máy tính số học bằng Python, mô hình hóa quá trình sinh học, phân tích dữ liệu thời tiết.</li>
                <li>Lập kế hoạch tự học và thực hành kỹ năng định kỳ hàng tuần.</li>
            </ul>
        </li>
    </ul>

    <h4>Tư duy sáng tạo và phản biện (Creative & Scientific Thinking):</h4>
    <ul>
        <li><strong>Điểm cao:</strong> Bạn thích đặt câu hỏi mới, dám thử giải pháp khác lạ, và có khả năng phân tích nhiều góc nhìn – đây là chìa khóa để làm nghiên cứu và phát triển tri thức mới.</li>
        <li><strong>Điểm chưa cao:</strong> Bạn có thể còn quen học theo mẫu, ngại sai, chưa quen đặt giả thuyết hoặc tìm phương án khác.</li>
        <li><strong>Gợi ý phát triển:</strong>
            <ul>
                <li>Thử xây dựng "Giả thuyết điên rồ" mỗi tuần và tìm cách chứng minh/nghiên cứu thử.</li>
                <li>Tham gia các cuộc thi sáng tạo khoa học (hackathon, nghiên cứu khoa học sinh viên, giải pháp xanh...)</li>
                <li>Viết bài phân tích so sánh các giả thuyết khoa học lịch sử với các mô hình hiện tại.</li>
                <li>Tập phát triển ý tưởng từ “hiện tượng đời sống” – ví dụ: tạo mô hình dự báo độ bụi, đánh giá hiệu quả khẩu trang, phân tích thời gian học và kết quả.</li>
            </ul>
        </li>
    </ul>

    <h4>Định hướng phát triển nghề nghiệp:</h4>
    <ul>
        <li>Chọn chuyên ngành phù hợp giữa các lĩnh vực Toán – Lý – Hóa – Sinh – Môi trường – Dữ liệu – Công nghệ.</li>
        <li>Tham gia các nhóm nghiên cứu sinh viên, CLB sáng tạo khoa học hoặc mô phỏng công trình nghiên cứu.</li>
        <li>Thực hiện nghiên cứu nhỏ với đề tài cá nhân hoặc nhóm: đo nhiệt độ lớp học, phân tích dữ liệu ô nhiễm, đo chất lượng nước,...</li>
        <li>Chuẩn bị hồ sơ học bổng hoặc thi học sinh giỏi, xét tuyển đại học bằng hồ sơ dự án thực tế.</li>
        <li>Phát triển kỹ năng học thuật (viết bài khoa học, phân tích, trích dẫn, tìm tài liệu học thuật hiệu quả).</li>
    </ul>

    <h4>Tài nguyên học tập gợi ý:</h4>
    <ul>
        <li>Website: Khan Academy, Brilliant.org, SciShow, Nature, Quanta Magazine.</li>
        <li>Podcast: The Infinite Monkey Cage, Science Vs, Orbital Mechanics Podcast.</li>
        <li>Sách: “Thinking Fast and Slow”, “A Brief History of Time”, “The Disappearing Spoon”, “Astrophysics for People in a Hurry”.</li>
        <li>Kênh Youtube: Veritasium, TED-Ed, Physics Girl, Crash Course, Numberphile.</li>
    </ul>

    <h4>Lời khuyên tổng kết:</h4>
    <p>Hãy duy trì sự tò mò và kỷ luật – bạn là kiểu người không chỉ học để biết, mà học để tạo ra sự hiểu biết mới. Khoa học sẽ đưa bạn tới những nơi chưa ai đặt chân – miễn là bạn dám đặt câu hỏi và đi đến cùng với nó. Một thói quen đọc mỗi ngày, một dự án mỗi quý, và một bài học từ mỗi thất bại sẽ tạo nên con đường khoa học vững chắc cho bạn.</p>
    """

}

# ==============================
# 🚩 Hàm generate_analysis_html cho TAB TỔNG QUAN
# ==============================
def generate_analysis_html_social(skill_scores, readiness_score):
    """
    Phân tích năng lực nhóm ngành Xã hội – Nhân văn.
    Nhận xét khái quát dựa trên điểm trung bình kỹ năng, không suy luận hành vi cụ thể.
    """

    def create_timeline_item(icon, title, description):
        return f"""
        <div class="timeline-item">
            <div class="timeline-marker">{icon}</div>
            <div class="timeline-content">
                <strong>{title}</strong>
                <span>{description}</span>
            </div>
        </div>
        """

    items_html = []

    # --- Kỹ năng mềm ---
    soft_skill = skill_scores.get("Kỹ năng mềm", 0)
    if soft_skill >= 80:
        items_html.append(create_timeline_item("🤝", "Kỹ năng mềm: Mạnh",
            "Bạn có nền tảng kỹ năng giao tiếp và hợp tác tốt – đây là điểm mạnh giúp bạn thích nghi và phát triển trong môi trường xã hội – nhân văn."))
    elif soft_skill >= 60:
        items_html.append(create_timeline_item("💬", "Kỹ năng mềm: Ổn định",
            "Bạn có nền kỹ năng mềm khá, nên tiếp tục rèn luyện thêm qua hoạt động nhóm, chia sẻ và học hỏi để nâng cao hiệu quả làm việc chung."))
    else:
        items_html.append(create_timeline_item("🛠️", "Kỹ năng mềm: Cần củng cố",
            "Bạn nên chú trọng hơn vào kỹ năng giao tiếp, hợp tác và phản hồi trong học tập và công việc. Việc tham gia nhóm học hoặc hoạt động cộng đồng sẽ giúp bạn tiến bộ."))

    # --- Kỹ năng chuyên môn ---
    tech_skill = skill_scores.get("Kỹ năng chuyên môn", 0)
    if tech_skill >= 80:
        items_html.append(create_timeline_item("📘", "Kỹ năng chuyên môn: Tốt",
            "Bạn có nền tảng chuyên môn vững chắc. Hãy tận dụng điều này để mở rộng thực hành, tham gia dự án thực tế và phát triển chuyên sâu."))
    elif tech_skill >= 60:
        items_html.append(create_timeline_item("📚", "Kỹ năng chuyên môn: Ở mức khá",
            "Bạn đã có nền chuyên môn cơ bản khá ổn định. Việc chủ động học hỏi thêm và tham gia hoạt động thực tiễn sẽ giúp bạn tự tin hơn."))
    else:
        items_html.append(create_timeline_item("📖", "Kỹ năng chuyên môn: Cần cải thiện",
            "Bạn cần bồi dưỡng thêm kiến thức ngành và kỹ năng vận dụng. Hãy bắt đầu bằng việc đọc tài liệu, học hỏi qua dự án nhỏ hoặc trao đổi với người có kinh nghiệm."))

    # --- Tư duy sáng tạo ---
    creative_skill = skill_scores.get("Tư duy sáng tạo", 0)
    if creative_skill >= 80:
        items_html.append(create_timeline_item("🌟", "Tư duy sáng tạo: Nổi bật",
            "Bạn có tiềm năng sáng tạo cao – một lợi thế lớn trong lĩnh vực giáo dục, truyền thông và xã hội. Hãy tiếp tục phát huy trong việc chia sẻ và trình bày ý tưởng."))
    elif creative_skill >= 60:
        items_html.append(create_timeline_item("💡", "Tư duy sáng tạo: Ổn định",
            "Bạn có nền tư duy sáng tạo khá, nên phát triển thêm bằng cách thử nghiệm cách học mới, ứng dụng công cụ số và chia sẻ kiến thức linh hoạt hơn."))
    else:
        items_html.append(create_timeline_item("📎", "Tư duy sáng tạo: Cần rèn luyện",
            "Bạn nên rèn luyện thêm khả năng tư duy linh hoạt, trình bày sinh động và sáng tạo. Đây là kỹ năng quan trọng để tạo dấu ấn riêng trong môi trường xã hội."))

    # --- Đánh giá chung ---
    if readiness_score >= 70:
        items_html.append(create_timeline_item("✅", "Tổng thể: Rất sẵn sàng",
            "Bạn có sự chuẩn bị toàn diện để theo đuổi ngành Xã hội – Nhân văn. Hãy mạnh dạn bước ra thực tiễn, tham gia dự án, thực tập hoặc hoạt động cộng đồng."))
    elif readiness_score >= 50:
        items_html.append(create_timeline_item("⚡", "Tổng thể: Ở mức khá",
            "Bạn đang có nền tảng tương đối tốt. Hãy tiếp tục rèn luyện, đặc biệt thông qua trải nghiệm thực tế để củng cố kỹ năng và định hướng phát triển."))
    else:
        items_html.append(create_timeline_item("🔄", "Tổng thể: Cần thêm thời gian",
            "Bạn cần thêm thời gian để phát triển kỹ năng nền. Hãy học từng bước, từ kiến thức cơ bản đến thực hành nhóm nhỏ – mỗi bước tiến đều có giá trị."))

    return f"<div class='analysis-timeline'>{''.join(items_html)}</div>"



def generate_analysis_html_business(skill_scores, readiness_score):
    """
    Phân tích kỹ năng cho nhóm ngành Kinh doanh – Quản lý.
    Nội dung mang tính tổng quát, không giả định ngành cụ thể hay hành vi người dùng.
    """

    def create_timeline_item(icon, title, description):
        return f"""
        <div class="timeline-item">
            <div class="timeline-marker">{icon}</div>
            <div class="timeline-content">
                <strong>{title}</strong>
                <span>{description}</span>
            </div>
        </div>
        """

    items_html = []

    # --- Kỹ năng mềm ---
    soft_skill = skill_scores.get("Kỹ năng mềm", 0)
    if soft_skill >= 80:
        items_html.append(create_timeline_item("💪", "Kỹ năng mềm: Mạnh",
            "Bạn có nền kỹ năng mềm tốt – đây là yếu tố quan trọng giúp bạn làm việc hiệu quả với người khác và thích nghi với môi trường năng động."))
    elif soft_skill >= 60:
        items_html.append(create_timeline_item("💡", "Kỹ năng mềm: Ổn định",
            "Bạn có kỹ năng giao tiếp và làm việc nhóm ở mức khá. Hãy tiếp tục rèn luyện để nâng cao sự tự tin, linh hoạt và khả năng kết nối."))
    else:
        items_html.append(create_timeline_item("🛠️", "Kỹ năng mềm: Cần phát triển thêm",
            "Bạn nên luyện tập thêm kỹ năng giao tiếp, phối hợp nhóm và xử lý tình huống. Đây là nền tảng quan trọng trong học tập và công việc thực tế."))

    # --- Kỹ năng chuyên môn ---
    tech_skill = skill_scores.get("Kỹ năng chuyên môn", 0)
    if tech_skill >= 80:
        items_html.append(create_timeline_item("📈", "Kỹ năng chuyên môn: Vững",
            "Bạn có nền kiến thức chuyên môn tốt và có khả năng ứng dụng vào thực tiễn. Hãy tiếp tục phát triển để nâng cao sự tự tin trong học tập và công việc."))
    elif tech_skill >= 60:
        items_html.append(create_timeline_item("📘", "Kỹ năng chuyên môn: Khá",
            "Bạn đã có nền kiến thức cơ bản tương đối ổn. Hãy chủ động mở rộng hiểu biết và luyện tập thêm để tăng khả năng vận dụng."))
    else:
        items_html.append(create_timeline_item("🔧", "Kỹ năng chuyên môn: Cần củng cố",
            "Bạn đang trong quá trình xây nền kiến thức chuyên môn. Hãy bắt đầu từ việc học thêm tài liệu, thảo luận nhóm và thử sức ở các hoạt động nhỏ."))

    # --- Tư duy sáng tạo ---
    creative_skill = skill_scores.get("Tư duy sáng tạo", 0)
    if creative_skill >= 80:
        items_html.append(create_timeline_item("✨", "Tư duy sáng tạo: Nổi bật",
            "Bạn có khả năng đưa ra ý tưởng mới và cách làm linh hoạt. Đây là lợi thế để thích nghi với thay đổi và tìm ra hướng đi mới mẻ trong công việc."))
    elif creative_skill >= 60:
        items_html.append(create_timeline_item("🖌️", "Tư duy sáng tạo: Ổn định",
            "Bạn có nền tư duy sáng tạo khá tốt. Hãy tiếp tục phát triển bằng cách tìm kiếm phương pháp mới và thử nghiệm trong các hoạt động học tập, dự án."))
    else:
        items_html.append(create_timeline_item("⚙️", "Tư duy sáng tạo: Cần rèn luyện",
            "Bạn nên dành thời gian rèn luyện khả năng sáng tạo – ví dụ qua việc quan sát, đặt câu hỏi mới và thử những cách học, cách làm khác nhau."))

    # --- Đánh giá tổng thể ---
    if readiness_score >= 70:
        items_html.append(create_timeline_item("✅", "Tổng thể: Sẵn sàng cao",
            "Bạn đã có sự chuẩn bị tốt để theo đuổi lĩnh vực Kinh doanh – Quản lý. Hãy mạnh dạn tham gia hoạt động thực tiễn để phát triển sâu hơn."))
    elif readiness_score >= 50:
        items_html.append(create_timeline_item("⚡", "Tổng thể: Ở mức khá",
            "Bạn có nền kỹ năng cơ bản và tiềm năng phát triển. Hãy tiếp tục rèn luyện qua trải nghiệm nhóm, dự án thực hành hoặc học từ thực tế."))
    else:
        items_html.append(create_timeline_item("🔄", "Tổng thể: Cần tích lũy thêm",
            "Bạn đang trong giai đoạn hoàn thiện kỹ năng. Hãy tập trung xây dựng nền tảng, chủ động học hỏi và từng bước nâng cao năng lực cá nhân."))

    return f"<div class='analysis-timeline'>{''.join(items_html)}</div>"



def generate_analysis_html_tech(skill_scores, readiness_score):
    """
    Phân tích kỹ năng tổng quát cho nhóm ngành Công nghệ – Kỹ thuật.
    Giao diện timeline, nội dung trung tính theo điểm kỹ năng.
    """

    def create_timeline_item(icon, title, description):
        return f"""
        <div class="timeline-item">
            <div class="timeline-marker">{icon}</div>
            <div class="timeline-content">
                <strong>{title}</strong>
                <span>{description}</span>
            </div>
        </div>
        """

    items_html = []

    # --- Kỹ năng mềm ---
    soft_skill = skill_scores.get("Kỹ năng mềm", 0)
    if soft_skill >= 80:
        items_html.append(create_timeline_item("🤝", "Kỹ năng mềm: Tốt",
            "Bạn có nền tảng giao tiếp, làm việc nhóm và phối hợp hiệu quả – rất cần thiết khi tham gia dự án hoặc xử lý vấn đề kỹ thuật cùng người khác."))
    elif soft_skill >= 60:
        items_html.append(create_timeline_item("💬", "Kỹ năng mềm: Ổn định",
            "Bạn đang có mức kỹ năng mềm khá. Hãy tiếp tục rèn luyện khả năng diễn đạt, trao đổi và hợp tác để làm việc kỹ thuật hiệu quả hơn trong môi trường thực tế."))
    else:
        items_html.append(create_timeline_item("🛠️", "Kỹ năng mềm: Cần cải thiện",
            "Bạn cần rèn thêm kỹ năng giao tiếp, phối hợp và phản hồi nhóm – yếu tố quan trọng để làm việc tốt trong lĩnh vực công nghệ – kỹ thuật."))

    # --- Kỹ năng chuyên môn ---
    tech_skill = skill_scores.get("Kỹ năng chuyên môn", 0)
    if tech_skill >= 80:
        items_html.append(create_timeline_item("📘", "Kỹ năng chuyên môn: Vững vàng",
            "Bạn có kiến thức và khả năng ứng dụng kỹ thuật tốt. Hãy tiếp tục củng cố thông qua thực hành, tham gia các dự án và cập nhật công nghệ thường xuyên."))
    elif tech_skill >= 60:
        items_html.append(create_timeline_item("📚", "Kỹ năng chuyên môn: Ở mức khá",
            "Bạn đã có nền kiến thức kỹ thuật cơ bản. Việc luyện tập thường xuyên, học thêm và thử nghiệm ứng dụng thực tế sẽ giúp bạn phát triển vững hơn."))
    else:
        items_html.append(create_timeline_item("📖", "Kỹ năng chuyên môn: Cần bồi dưỡng",
            "Bạn đang trong giai đoạn xây dựng kiến thức nền. Hãy tập trung học theo lộ trình rõ ràng và tăng cường thực hành để hiểu và ứng dụng hiệu quả hơn."))

    # --- Tư duy sáng tạo ---
    creative_skill = skill_scores.get("Tư duy sáng tạo", 0)
    if creative_skill >= 80:
        items_html.append(create_timeline_item("💡", "Tư duy sáng tạo: Nổi bật",
            "Bạn có khả năng suy nghĩ linh hoạt, đưa ra hướng tiếp cận mới – đây là yếu tố then chốt trong việc phát triển giải pháp kỹ thuật hiệu quả và sáng tạo."))
    elif creative_skill >= 60:
        items_html.append(create_timeline_item("🖌️", "Tư duy sáng tạo: Ổn định",
            "Bạn có tư duy đổi mới ở mức khá. Hãy tiếp tục quan sát, học hỏi và thử nghiệm nhiều hướng giải quyết vấn đề để tăng độ linh hoạt trong kỹ thuật."))
    else:
        items_html.append(create_timeline_item("⚙️", "Tư duy sáng tạo: Đang phát triển",
            "Bạn cần luyện thêm khả năng sáng tạo kỹ thuật. Hãy bắt đầu bằng cách phân tích vấn đề đa chiều, tìm hiểu giải pháp khác nhau và quan sát cách người khác làm."))

    # --- Đánh giá tổng thể ---
    if readiness_score >= 70:
        items_html.append(create_timeline_item("✅", "Tổng thể: Rất sẵn sàng",
            "Bạn đã có sự chuẩn bị tốt để theo đuổi ngành Công nghệ – Kỹ thuật. Hãy mạnh dạn tham gia các hoạt động thực hành, dự án hoặc nghiên cứu để phát triển sâu hơn."))
    elif readiness_score >= 50:
        items_html.append(create_timeline_item("⚡", "Tổng thể: Ở mức khá",
            "Bạn đang có nền tảng kỹ năng khá toàn diện. Hãy rèn luyện thêm qua dự án nhóm, thực hành kỹ thuật và học hỏi kinh nghiệm từ người khác."))
    else:
        items_html.append(create_timeline_item("🔄", "Tổng thể: Cần tích lũy thêm",
            "Bạn cần thêm thời gian để phát triển kỹ năng và kiến thức. Hãy bắt đầu từ những dự án nhỏ, khóa học cơ bản và môi trường học tập thân thiện để từng bước tiến bộ."))

    return f"<div class='analysis-timeline'>{''.join(items_html)}</div>"



def generate_analysis_html_science(skill_scores, readiness_score):
    """
    Phân tích năng lực nhóm ngành Khoa học – Tự nhiên.
    Giao diện Timeline tinh gọn, nội dung sát với bộ câu hỏi trắc nghiệm đánh giá kỹ năng.
    """

    def create_timeline_item(icon, title, description):
        return f"""
        <div class="timeline-item">
            <div class="timeline-marker">{icon}</div>
            <div class="timeline-content">
                <strong>{title}</strong>
                <span>{description}</span>
            </div>
        </div>
        """

    items_html = []

    # --- Kỹ năng mềm ---
    soft_skill = skill_scores.get("Kỹ năng mềm", 0)
    if soft_skill >= 80:
        items_html.append(create_timeline_item("🤝", "Kỹ năng mềm: Rất tốt",
            "Bạn có khả năng làm việc nhóm, thuyết trình, giao tiếp học thuật tốt. Đây là nền tảng để tham gia nghiên cứu nhóm, phản biện và trình bày trước hội đồng."))
    elif soft_skill >= 60:
        items_html.append(create_timeline_item("💬", "Kỹ năng mềm: Ở mức khá",
            "Bạn có sự hợp tác và tự tin nhất định. Hãy chủ động hơn trong thảo luận nhóm, đặt câu hỏi, phản biện và rèn kỹ năng thuyết trình trong môi trường học thuật."))
    else:
        items_html.append(create_timeline_item("🛠️", "Kỹ năng mềm: Cần rèn luyện",
            "Bạn còn hạn chế trong tương tác nhóm và giao tiếp học thuật. Hãy tham gia workshop, CLB nghiên cứu hoặc học qua video mô phỏng phản biện khoa học để cải thiện."))

    # --- Kỹ năng chuyên môn ---
    tech_skill = skill_scores.get("Kỹ năng chuyên môn", 0)
    if tech_skill >= 80:
        items_html.append(create_timeline_item("📘", "Kỹ năng chuyên môn: Vững vàng",
            "Bạn nắm chắc kiến thức chuyên ngành, biết lên kế hoạch nghiên cứu và thành thạo công cụ xử lý dữ liệu. Bạn hoàn toàn sẵn sàng tham gia đề tài nghiên cứu sinh viên."))
    elif tech_skill >= 60:
        items_html.append(create_timeline_item("🧪", "Kỹ năng chuyên môn: Tương đối tốt",
            "Bạn có kiến thức nền ổn định và đã làm quen với nghiên cứu. Hãy luyện tập thêm việc trình bày báo cáo, đọc tài liệu tiếng Anh và thử nghiệm phân tích số liệu thực tế."))
    else:
        items_html.append(create_timeline_item("🔍", "Kỹ năng chuyên môn: Cần củng cố",
            "Bạn cần củng cố kiến thức nền, rèn kỹ năng đọc tài liệu chuyên ngành, phân tích số liệu đơn giản và viết báo cáo theo cấu trúc khoa học chuẩn."))

    # --- Tư duy sáng tạo ---
    creative_skill = skill_scores.get("Tư duy sáng tạo", 0)
    if creative_skill >= 80:
        items_html.append(create_timeline_item("🌟", "Tư duy sáng tạo: Nổi bật",
            "Bạn thường xuyên đưa ra ý tưởng mới, cải tiến phương pháp nghiên cứu và có tư duy phản biện. Hãy thử sức với đề tài liên ngành hoặc đổi mới quy trình nghiên cứu."))
    elif creative_skill >= 60:
        items_html.append(create_timeline_item("💡", "Tư duy sáng tạo: Có tiềm năng",
            "Bạn có khả năng đặt câu hỏi, tìm cách cải tiến nhưng chưa thường xuyên. Hãy tăng cường ứng dụng công cụ số, đặt giả thuyết và thử nghiệm nhiều cách giải quyết vấn đề."))
    else:
        items_html.append(create_timeline_item("📎", "Tư duy sáng tạo: Đang phát triển",
            "Bạn có xu hướng làm theo hướng dẫn. Hãy luyện tập đặt câu hỏi 'Vì sao?', 'Nếu thay đổi... thì sao?', và thử sáng tạo khi viết báo cáo hoặc tối ưu quy trình học tập."))

        # --- Đánh giá chung theo readiness_score ---
    if readiness_score >= 70:
        items_html.append(create_timeline_item("✅", "Đánh giá chung: Rất sẵn sàng",
            "Bạn đã sẵn sàng để tham gia vào môi trường học thuật và nghiên cứu khoa học. "
            "Hãy tận dụng thời điểm này để chủ động đăng ký đề tài, viết báo cáo khoa học, tham dự hội thảo chuyên ngành hoặc các buổi chia sẻ học thuật. "
            "Việc kết nối với giảng viên, mentor và cộng đồng nghiên cứu sẽ giúp bạn tiến xa hơn trong hành trình khoa học."))
        
    elif readiness_score >= 50:
        items_html.append(create_timeline_item("⚡", "Đánh giá chung: Sẵn sàng ở mức khá",
            "Bạn đang có nền tảng tốt để bắt đầu tham gia nghiên cứu. "
            "Hãy tập trung luyện kỹ năng lập kế hoạch, thực hiện thí nghiệm nhỏ, xử lý dữ liệu cơ bản và viết báo cáo theo chuẩn học thuật. "
            "Việc thực hành từng bước sẽ giúp bạn hình thành tư duy khoa học và nâng cao năng lực nghiên cứu."))
        
    else:
        items_html.append(create_timeline_item("🔄", "Đánh giá chung: Cần nỗ lực thêm",
            "Bạn đang ở giai đoạn khởi đầu, cần củng cố cả kỹ năng và tư duy học thuật. "
            "Hãy bắt đầu bằng việc tham gia workshop, đọc tài liệu khoa học đơn giản, luyện viết báo cáo ngắn và làm quen với công cụ như Excel, Python hoặc SPSS. "
            "Duy trì sự tò mò, chủ động học hỏi và tiến bộ từng bước chính là điều quan trọng nhất trong hành trình này."))

    return f"<div class='analysis-timeline'>{''.join(items_html)}</div>"


def generate_analysis_html_health(skill_scores, readiness_score):
    """
    Phân tích kỹ năng tổng quát cho nhóm ngành Y tế – Sức khỏe.
    Giao diện timeline, nội dung trung lập, phù hợp nhiều ngành nhỏ.
    """

    def create_timeline_item(icon, title, description):
        return f"""
        <div class="timeline-item">
            <div class="timeline-marker">{icon}</div>
            <div class="timeline-content">
                <strong>{title}</strong>
                <span>{description}</span>
            </div>
        </div>
        """

    items_html = []

    # --- Kỹ năng mềm ---
    soft_skill = skill_scores.get("Kỹ năng mềm", 0)
    if soft_skill >= 80:
        items_html.append(create_timeline_item("💬", "Kỹ năng mềm: Rất tốt",
            "Bạn có khả năng giao tiếp, lắng nghe và phối hợp hiệu quả với người khác – đây là nền tảng quan trọng trong mọi lĩnh vực thuộc nhóm ngành Y tế – Sức khỏe."))
    elif soft_skill >= 60:
        items_html.append(create_timeline_item("🤝", "Kỹ năng mềm: Ổn định",
            "Bạn đã có kỹ năng mềm khá tốt. Hãy tiếp tục phát triển khả năng làm việc nhóm, phản hồi tình huống và kết nối trong môi trường chuyên môn."))
    else:
        items_html.append(create_timeline_item("🛠️", "Kỹ năng mềm: Cần rèn luyện",
            "Bạn nên tăng cường khả năng giao tiếp, phối hợp và thấu hiểu – những yếu tố giúp bạn thích nghi hiệu quả trong môi trường làm việc với con người."))

    # --- Kỹ năng chuyên môn ---
    tech_skill = skill_scores.get("Kỹ năng chuyên môn", 0)
    if tech_skill >= 80:
        items_html.append(create_timeline_item("📘", "Kỹ năng chuyên môn: Vững vàng",
            "Bạn có nền kiến thức chuyên môn tốt và biết cách áp dụng vào thực tế. Hãy tiếp tục học hỏi và mở rộng hiểu biết trong lĩnh vực bạn theo đuổi."))
    elif tech_skill >= 60:
        items_html.append(create_timeline_item("📚", "Kỹ năng chuyên môn: Khá",
            "Bạn có nền tảng ổn định. Việc duy trì việc học đều đặn, thực hành thường xuyên và tiếp cận đa chiều sẽ giúp bạn phát triển sâu hơn."))
    else:
        items_html.append(create_timeline_item("📖", "Kỹ năng chuyên môn: Cần củng cố",
            "Bạn cần bồi dưỡng thêm kiến thức nền và kỹ năng chuyên ngành. Hãy bắt đầu từ những khái niệm cơ bản và thực hành có hướng dẫn để tiến bộ rõ rệt."))

    # --- Tư duy sáng tạo ---
    creative_skill = skill_scores.get("Tư duy sáng tạo", 0)
    if creative_skill >= 80:
        items_html.append(create_timeline_item("✨", "Tư duy sáng tạo: Tốt",
            "Bạn có khả năng linh hoạt trong cách nghĩ và tìm ra giải pháp mới – một phẩm chất quý giá trong bối cảnh ngành y tế đang không ngừng thay đổi."))
    elif creative_skill >= 60:
        items_html.append(create_timeline_item("💡", "Tư duy sáng tạo: Ổn định",
            "Bạn có khả năng quan sát, đặt câu hỏi và cải tiến cách học, cách làm. Hãy tiếp tục phát huy để thích nghi tốt hơn với các tình huống khác nhau."))
    else:
        items_html.append(create_timeline_item("⚙️", "Tư duy sáng tạo: Cần phát triển",
            "Bạn nên rèn luyện cách suy nghĩ mở, tiếp cận vấn đề theo nhiều hướng và dần hình thành thói quen đặt câu hỏi, đề xuất cải tiến nhỏ trong công việc."))

    # --- Đánh giá tổng thể ---
    if readiness_score >= 70:
        items_html.append(create_timeline_item("✅", "Tổng thể: Đã sẵn sàng",
            "Bạn có nền kỹ năng và tư duy phù hợp để tiếp tục phát triển trong lĩnh vực Y tế – Sức khỏe. Hãy tích cực học hỏi từ trải nghiệm thực tế và mở rộng kết nối chuyên môn."))
    elif readiness_score >= 50:
        items_html.append(create_timeline_item("⚡", "Tổng thể: Ở mức khá",
            "Bạn đang trên hành trình tích lũy khá tốt. Hãy chủ động thực hành, rèn kỹ năng nền và tham gia các hoạt động học tập có tính ứng dụng."))
    else:
        items_html.append(create_timeline_item("🔄", "Tổng thể: Cần tích lũy thêm",
            "Bạn đang xây dựng nền tảng. Hãy bắt đầu từ việc rèn luyện kỹ năng cơ bản, củng cố kiến thức chuyên môn và từng bước tham gia các hoạt động đơn giản để nâng cao sự tự tin."))

    return f"<div class='analysis-timeline'>{''.join(items_html)}</div>"



def generate_analysis_html_arts(skill_scores, readiness_score):
    """
    Phân tích kỹ năng cho nhóm ngành Nghệ thuật – Sáng tạo.
    Dạng timeline. Nội dung mang tính khái quát, phù hợp với các ngành nghệ thuật khác nhau.
    """

    def create_timeline_item(icon, title, description):
        return f"""
        <div class="timeline-item">
            <div class="timeline-marker">{icon}</div>
            <div class="timeline-content">
                <strong>{title}</strong>
                <span>{description}</span>
            </div>
        </div>
        """

    items_html = []

    # --- Kỹ năng mềm ---
    soft_skill = skill_scores.get("Kỹ năng mềm", 0)
    if soft_skill >= 80:
        items_html.append(create_timeline_item("🎤", "Kỹ năng mềm: Rất tốt",
            "Bạn có khả năng giao tiếp sáng rõ, trình bày ý tưởng thuyết phục, phối hợp nhóm hiệu quả – đây là yếu tố then chốt khi làm việc trong môi trường sáng tạo và trưng bày sản phẩm."))
    elif soft_skill >= 60:
        items_html.append(create_timeline_item("🤝", "Kỹ năng mềm: Ở mức khá",
            "Bạn có nền kỹ năng mềm ổn định, cần tiếp tục rèn luyện kỹ năng phản hồi trong nhóm, trình bày ý tưởng, và giao tiếp tự tin hơn trong các sự kiện hoặc với khách hàng."))
    else:
        items_html.append(create_timeline_item("🛠️", "Kỹ năng mềm: Cần phát triển",
            "Bạn nên trau dồi kỹ năng làm việc nhóm, quản lý thời gian, và tự tin chia sẻ ý tưởng. Đây là yếu tố cơ bản trong quá trình thực hiện và trình bày tác phẩm."))

    # --- Kỹ năng chuyên môn ---
    tech_skill = skill_scores.get("Kỹ năng chuyên môn", 0)
    if tech_skill >= 80:
        items_html.append(create_timeline_item("🎨", "Kỹ năng chuyên môn: Vững vàng",
            "Bạn có kỹ năng chuyên ngành tốt, sử dụng thành thạo công cụ thiết kế và hoàn thiện sản phẩm chuyên nghiệp. Hãy tiếp tục thử nghiệm để nâng cao phong cách cá nhân."))
    elif tech_skill >= 60:
        items_html.append(create_timeline_item("📘", "Kỹ năng chuyên môn: Ổn định",
            "Bạn đã có nền tảng kỹ năng tốt, cần chủ động tham gia thêm các cuộc thi, triển lãm hoặc dự án sáng tạo để rèn luyện khả năng ứng dụng và tinh chỉnh sản phẩm."))
    else:
        items_html.append(create_timeline_item("🔧", "Kỹ năng chuyên môn: Cần rèn luyện thêm",
            "Bạn nên tập trung học thêm về công cụ sáng tạo, kỹ năng chỉnh sửa và hoàn thiện sản phẩm. Tham gia CLB nghệ thuật hoặc dự án nhỏ sẽ giúp bạn tiến bộ nhanh hơn."))

    # --- Tư duy sáng tạo ---
    creative_skill = skill_scores.get("Tư duy sáng tạo", 0)
    if creative_skill >= 80:
        items_html.append(create_timeline_item("💡", "Tư duy sáng tạo: Nổi bật",
            "Bạn có khả năng đưa ra nhiều ý tưởng mới, thường xuyên cải tiến sản phẩm, tìm giải pháp sáng tạo và cập nhật xu hướng nghệ thuật – một lợi thế lớn trong ngành."))
    elif creative_skill >= 60:
        items_html.append(create_timeline_item("🧠", "Tư duy sáng tạo: Có tiềm năng",
            "Bạn có xu hướng sáng tạo tốt, nhưng cần chủ động hơn trong thử nghiệm ý tưởng và phát triển nội dung mới. Hãy học hỏi thêm từ các sản phẩm nghệ thuật đa dạng."))
    else:
        items_html.append(create_timeline_item("📎", "Tư duy sáng tạo: Đang phát triển",
            "Bạn cần luyện tập khả năng quan sát, phân tích và đề xuất giải pháp mới trong quá trình sáng tác. Việc tham khảo sản phẩm khác sẽ giúp bạn phát triển tư duy sáng tạo."))

    # --- Đánh giá tổng thể ---
    if readiness_score >= 70:
        items_html.append(create_timeline_item("✅", "Tổng thể: Rất sẵn sàng",
            "Bạn đã có sự chuẩn bị tốt về kỹ năng và tư duy cho lĩnh vực Nghệ thuật – Sáng tạo. Hãy tiếp tục xây dựng sản phẩm cá nhân, tham gia workshop và mở rộng mạng lưới cộng đồng."))
    elif readiness_score >= 50:
        items_html.append(create_timeline_item("⚡", "Tổng thể: Ở mức khá",
            "Bạn có nền kỹ năng cần thiết, cần tăng cường trải nghiệm thực tế, làm dự án nhóm hoặc tham gia các hoạt động nghệ thuật để phát triển thêm kỹ năng chuyên môn."))
    else:
        items_html.append(create_timeline_item("🔄", "Tổng thể: Cần phát triển thêm",
            "Bạn đang ở giai đoạn xây nền. Hãy bắt đầu từ những kỹ năng cơ bản, học cách sử dụng phần mềm thiết kế, tìm hiểu về quy trình sáng tác và rèn luyện đều đặn mỗi ngày."))

    return f"<div class='analysis-timeline'>{''.join(items_html)}</div>"


# ==============================
# 🚩 Hàm get_detailed_analysis_html cho TAB PHÂN TÍCH CHI TIẾT
# ==============================
def generate_detailed_analysis_html(cluster_code, skill_scores=None, readiness_score=None):
    template = ANALYSIS_HTMLS.get(cluster_code)
    if not template:
        return "<p>Hiện chưa có nội dung phân tích chi tiết cho nhóm ngành này.</p>"
    return template



# ==============================
# ✅ Cách sử dụng trong views.py:
# from .generate_analysis_html import generate_analysis_html, get_detailed_analysis_html
# và gọi:
# analysis_html = generate_analysis_html(skill_scores, readiness_score)
# detailed_analysis_html = get_detailed_analysis_html(cluster_code, readiness_score)
# ==============================
