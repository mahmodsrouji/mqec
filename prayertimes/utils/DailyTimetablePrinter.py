from django.template.loader import render_to_string
from datetime import datetime

# نفترض أنّ هناك فئة أساسية (base class) باسم TimetablePrinter
# ودالة مساعدة DPTHelper تم تحويلها أيضًا إلى Python
from .timetable_printer import TimetablePrinter
from ..models.dpt_helper import DPTHelper

class DailyTimetablePrinter(TimetablePrinter):
    def __init__(self):
        super().__init__()
        # نفترض أنّ الدالة get_local_prayer_names مُنفذة في الفئة الأم أو هنا
        self.local_prayer_names = self.get_local_prayer_names(False, True)
        self.dpt_helper = DPTHelper()

    def horizontal_time_div(self, row):
        # بدلاً من استخدام ob_start و include، نقوم بعرض قالب Django
        # يجب إنشاء قالب "horizontal-div.html" في مجلد templates
        return render_to_string('horizontal-div.html', {'row': row})

    def print_horizontal_time(self, row):
        table = self.print_horizontal_table_top(row)
        table += f'''
            <tr>
                <th class="tableHeading prayerName">{self.local_headers['prayer']}</th>
                {self.print_table_heading(row)}
            </tr>
            <tr>
                <th class="tableHeading">{self.local_headers['begins']}</th>
                {self.print_azan_time(row)}
            </tr>
            <tr>
                <th class="tableHeading">{self.local_headers['iqamah']}</th>
                {self.print_jamah_time(row, False)}
            </tr>
        '''
        if self.get_option('jumuah1') and not self.today_is_friday():
            table += f'''
                <tr>
                    <th class="tableHeading">{self.get_local_headers()['jumuah']}</th>
                    <td colspan="6" class="jamah">{self.get_jumuah_times_array()}</td>
                </tr>
            '''
        table += '</table>'
        return table

    def horizontal_time_jamah_only(self, row):
        table = self.print_horizontal_table_top(row)
        table += f'''
            <tr>
                <th>{self.local_headers['prayer']}</th>
                {self.print_table_heading(row)}
            </tr>
            <tr>
                <th>{self.local_headers['iqamah']}</th>
                {self.print_jamah_time(row)}
            </tr>
        </table>
        '''
        return table

    def horizontal_time_azan_only(self, row):
        table = self.print_horizontal_table_top(row, is_azan_only=True)
        table += f'''
            <tr>
                <th>{self.local_headers['prayer']}</th>
                {self.print_table_heading(row)}
            </tr>
            <tr>
                <th>{self.local_headers['begins']}</th>
                {self.print_azan_time(row)}
            </tr>
        </table>
        '''
        return table

    def print_vertical_time(self, row):
        table = self.print_vertical_table_top(row, is_full_table=True)
        table += f'''
            <tr>
                <th class="tableHeading">{self.local_headers['prayer']}</th>
                <th class="tableHeading">{self.local_headers['begins']}</th>
                <th class="tableHeading">{self.local_headers['iqamah']}</th>
            </tr>
            {self.print_vertical_row(row, 'both')}
        </table>
        '''
        return table

    def vertical_time_jamah_only(self, row):
        table = self.print_vertical_table_top(row)
        table += f'''
            <tr>
                <th class="tableHeading">{self.local_headers['prayer']}</th>
                <th class="tableHeading">{self.local_headers['iqamah']}</th>
            </tr>
            {self.print_vertical_row(row, 'iqamah')}
        </table>
        '''
        return table

    def vertical_time_azan_only(self, row):
        table = self.print_vertical_table_top(row, is_full_table=False, is_azan_only=True)
        table += f'''
            <tr>
                <th class="tableHeading">{self.local_headers['prayer']}</th>
                <th class="tableHeading">{self.local_headers['begins']}</th>
            </tr>
            {self.print_vertical_row(row, 'azan')}
        </table>
        '''
        return table

    def print_horizontal_table_top(self, row, is_azan_only=False):
        announcement = ''
        next_iqamah = ''
        if not row.get('hideTimeRemaining'):
            if not is_azan_only:
                next_iqamah = self.get_next_iqamah_time(row)
        colspan = 7
        ramadan_tds = '<td></td>'

        ramadan = ''
        if self.is_ramadan() and not row.get('hideRamadan'):
            ramadan = f'''
                <tr class="">
                    <td colspan="3" class="highlight">{self.local_headers['fast_begins']}: {self.format_date_for_prayer(row.get('fajr_begins'), True)}</td>
                    {ramadan_tds}
                    <td colspan="3" class="highlight">{self.local_headers['fast_ends']}: {self.format_date_for_prayer(row.get('maghrib_begins'))}</td>
                </tr>
            '''
        if row.get('announcement'):
            announcement = f"<tr><th colspan='{colspan}' style='text-align:center' class='notificationBackground notificationFont'>{row.get('announcement')}</th></tr>"
        table = f'''
            <table class="customStyles dptUserStyles dptTimetable {self.get_table_class()}">
            {announcement}
            <tr>
             <th colspan="{colspan}" style="text-align:center">
                {row.get('widgetTitle')} {self.get_date_format()} {self.get_hijri_date(datetime.now())} {next_iqamah}
             </th>
            </tr>
            {ramadan}
        '''
        return table

    def display_ramadan_time(self, row):
        return f'''
            <table class="customStyles dptUserStyles">
                <tr style="text-align:center">
                    <td colspan="3" class="fasting highlight">{self.local_headers['fast_begins']}: {self.format_date_for_prayer(row.get('fajr_begins'), True)}</td>
                    <td style="border:0px;"></td>
                    <td colspan="3" class="fasting highlight">{self.local_headers['fast_ends']}: {self.format_date_for_prayer(row.get('maghrib_begins'))}</td>
                </tr>
            </table>
        '''

    def print_table_heading(self, row):
        ths = ''
        next_prayer = self.get_next_prayer(row)
        local_prayer_names = self.local_prayer_names.copy()
        if self.get_option('zawal'):
            local_prayer_names = self.toggle_sunrise_zawal(row, local_prayer_names)
        for key, prayer_name in local_prayer_names.items():
            class_attr = 'highlight' if next_prayer == key else ''
            ths += f"<th class='tableHeading prayerName {self.get_table_class()} {class_attr}'>{prayer_name}</th>"
        return ths

    def toggle_sunrise_zawal(self, row, prayer_names):
        if self.dpt_helper.is_zawal_time_next(row):
            prayer_names['sunrise'] = prayer_names.get('zawal', '')
            prayer_names.pop('zawal', None)
        else:
            prayer_names.pop('zawal', None)
        return prayer_names

    def print_azan_time(self, row):
        tds = ''
        next_prayer = self.get_next_prayer(row)
        azan_timings = self.get_azan_time(row)
        if self.get_option('zawal'):
            if self.dpt_helper.is_zawal_time_next(row):
                azan_timings['sunrise'] = self.dpt_helper.get_zawal_time(azan_timings.get('zuhr'))
        for key, azan in azan_timings.items():
            class_attr = 'highlight' if next_prayer == key else ''
            rowspan = "rowspan='2'" if key == 'sunrise' else ''
            tds += f"<td {rowspan} {class_attr}>{self.get_formatted_date_for_prayer(azan, key)}</td>"
        return tds

    def print_jamah_time(self, row, is_sunrise=True):
        jamah_times = self.get_jamah_time(row)
        if self.get_option('zawal'):
            if self.dpt_helper.is_zawal_time_next(row):
                jamah_times['sunrise'] = self.dpt_helper.get_zawal_time(row.get('zuhr_begins'))
        if not is_sunrise:
            jamah_times.pop('sunrise', None)
        tds = ''
        next_prayer = self.get_next_prayer(row)
        for key, time in jamah_times.items():
            class_attr = 'highlight' if next_prayer == key else 'jamah'
            tds += f"<td class='{class_attr}'>{self.get_formatted_date_for_prayer(time, key, True)}</td>"
        return tds

    def print_vertical_table_top(self, row, is_full_table=False, is_azan_only=False):
        next_iqamah = ''
        if not row.get('hideTimeRemaining'):
            if not is_azan_only:
                next_iqamah = self.get_next_iqamah_time(row)
        colspan = 3 if is_full_table else 2
        colspan_ramadan = "colspan='2'" if is_full_table else ''
        ramadan = ''
        if self.is_ramadan() and not row.get('hideRamadan'):
            ramadan = f'''
            <tr>
             <th class="highlight">{self.local_headers['fast_begins']}</th>
             <th {colspan_ramadan} class="highlight">{self.format_date_for_prayer(row.get('fajr_begins'), True)}</th>
            </tr>
            <tr>
             <th class="highlight">{self.local_headers['fast_ends']}</th>
             <th {colspan_ramadan} class="highlight">{self.format_date_for_prayer(row.get('maghrib_begins'))}</th>
            </tr>
            '''
        announcement = ''
        if row.get('announcement'):
            announcement = f"<tr><th colspan={colspan} style='text-align:center' class='notificationBackground notificationFont'>{row.get('announcement')}</th></tr>"
        table = f'''
            <table class="dptTimetable {self.get_table_class()} customStyles dptUserStyles">
            {announcement}
            <tr>
             <th colspan={colspan} style="text-align:center">
                {row.get('widgetTitle')} {self.get_date_format()} {self.get_hijri_date(datetime.now())} {next_iqamah}
             </th>
            </tr>
            {ramadan}
        '''
        return table

    def print_vertical_row(self, row, display):
        trs = ''
        next_prayer = self.get_next_prayer(row)
        local_prayer_names = self.local_prayer_names.copy()
        if self.get_option('zawal'):
            if self.dpt_helper.is_zawal_time_next(row):
                local_prayer_names = self.toggle_sunrise_zawal(row, local_prayer_names)
                row['sunrise'] = self.dpt_helper.get_zawal_time(row.get('zuhr_begins'))
            else:
                local_prayer_names.pop('zawal', None)
        for key, prayer_name in local_prayer_names.items():
            begins = f"{key.lower()}_begins" if key != 'sunrise' else 'sunrise'
            jamah = f"{key.lower()}_jamah" if key != 'sunrise' else 'sunrise'
            class_attr = 'highlight' if next_prayer == key else ''
            highlight_for_jamah = 'highlight' if next_prayer == key else ''
            trs += f'''
                <tr>
                    <th class="prayerName {class_attr}">{prayer_name}</th>
            '''
            if key == 'sunrise' and display == 'both':
                trs += f"<td colspan='2' class='{class_attr}'>{self.get_formatted_date_for_prayer(row.get(jamah), key)}</td>"
            elif display == 'azan':
                trs += f"<td class='begins {class_attr}'>{self.get_formatted_date_for_prayer(row.get(begins), key)}</td>"
            elif display == 'iqamah':
                trs += f"<td class='begins {class_attr}'>{self.get_formatted_date_for_prayer(row.get(jamah), key, True)}</td>"
            else:
                trs += f"<td class='begins {class_attr}'>{self.get_formatted_date_for_prayer(row.get(begins), key)}</td>"
                trs += f"<td class='jamah {highlight_for_jamah}'>{self.get_formatted_date_for_prayer(row.get(jamah), key, True)}</td>"
            trs += '</tr>'
        if self.get_option('jumuah1') and not self.today_is_friday():
            trs += f'''
                <tr>
                    <th class="prayerName"><span>{self.get_local_headers().get('jumuah')}</span></th>
                    <td colspan="2" class="jamah">{self.get_jumuah_times_array()}</td>
                </tr>
            '''
        return trs

    def get_formatted_date_for_prayer(self, time, prayer_name, is_jamah_time=False):
        jumuah_time = self.get_option('jumuah1')
        if prayer_name == 'zuhr' and self.today_is_friday() and is_jamah_time and jumuah_time:
            return self.get_jumuah_times_array()
        return self.format_date_for_prayer(time)

    def display_next_prayer(self, row):
        return self.get_next_iqamah_time(row)
