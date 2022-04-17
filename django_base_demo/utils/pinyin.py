import re

from pypinyin import pinyin, lazy_pinyin, Style, load_phrases_dict, load_single_dict


class Pinyin:
    """
    拼音帮助类
    """

    @staticmethod
    def get_pinyin(words, is_split=False, v_to_u=False, is_trim=True, connector='', to_lower=False, to_upper=False):
        """
        获取拼音，不带声调

        :param words: 汉字
        :param is_split: 是否按照空格分隔成数组
        :param v_to_u: 无声调相关拼音风格下的结果是否使用 ü 代替原来的 v，当为 False 时结果中将使用 v 表示 ü
        :param is_trim: 删除空白符
        :param connector: 连接符
        :param to_lower: 是否转小写
        :param to_upper: 是否转大写
        :return:
        """

        if not words:
            return ''

        if type(words) == str and is_split:
            words = words.split(' ')

        pinyin_list = lazy_pinyin(words, v_to_u=v_to_u)

        if is_trim:
            pinyin_list = [re.sub(re.compile(r'\s+'), '', x) for x in pinyin_list if re.sub(re.compile(r'\s+'), '', x)]

        words = connector.join(pinyin_list)

        if to_lower:
            words = words.lower()
        elif to_upper:
            words = words.upper()

        return words

    @staticmethod
    def get_pinyin_tone(words, is_split=False, v_to_u=False, is_trim=True, connector='', to_lower=False,
                        to_upper=False):
        """
        获取拼音，带声调

        :param words: 汉字
        :param is_split: 是否按照空格分隔成数组
        :param v_to_u: 无声调相关拼音风格下的结果是否使用 ü 代替原来的 v，当为 False 时结果中将使用 v 表示 ü
        :param is_trim: 删除空白符
        :param connector: 连接符
        :param to_lower: 是否转小写
        :param to_upper: 是否转大写
        :return:
        """

        if not words:
            return ''

        if type(words) == str and is_split:
            words = words.split(' ')

        pinyin_list = lazy_pinyin(words, style=Style.TONE, v_to_u=v_to_u)

        if is_trim:
            pinyin_list = [re.sub(re.compile(r'\s+'), '', x) for x in pinyin_list if re.sub(re.compile(r'\s+'), '', x)]

        words = connector.join(pinyin_list)

        if to_lower:
            words = words.lower()
        elif to_upper:
            words = words.upper()

        return words

    @staticmethod
    def get_pinyin_initial(words, is_split=False, is_trim=True, connector='', to_lower=False, to_upper=False):
        """
        获取拼音首字母

        :param words: 汉字
        :param is_split: 是否按照空格分隔成数组
        :param is_trim: 删除空白符
        :param connector: 连接符
        :param to_lower: 是否转小写
        :param to_upper: 是否转大写
        :return:
        """

        if not words:
            return ''

        if type(words) == str and is_split:
            words = words.split(' ')

        pinyin_list = lazy_pinyin(words, style=Style.FIRST_LETTER)

        if is_trim:
            pinyin_list = [re.sub(re.compile(r'\s+'), '', x) for x in pinyin_list if re.sub(re.compile(r'\s+'), '', x)]

        words = connector.join(pinyin_list)

        if to_lower:
            words = words.lower()
        elif to_upper:
            words = words.upper()

        return words


if __name__ == '__main__':
    """
    测试常用场景，详情参考文档：https://pypi.org/project/pypinyin/
    """

    # 自定义拼音库，用来修正结果，比如：换行（huan hang) 默认转成：huan xing
    load_phrases_dict({'换行': [['huàn'], ['háng']]})  # 自定义词组
    load_single_dict({ord('还'): 'hái,huán'})  # 调整 "还" 字的拼音顺序或覆盖默认拼音

    print(Pinyin.get_pinyin_tone("""
        二十 女性  努力 中心 
        ABC    
        abc      
               123456
        还
        音乐
        快乐
        换行
    """, is_split=False, v_to_u=True, connector='_'))

    pinyin('二个2个 中心')  # or pinyin(['中心'])，参数值为列表时表示输入的是已分词后的数据
    # [['èr'], ['gè'], ['2'], ['gè'], [' '], ['zhōng'], ['xīn']]

    pinyin('二个2个 中心', heteronym=True)  # 启用多音字模式
    # [['èr'], ['gè', 'gě', 'gàn'], ['2'], ['gè', 'gě', 'gàn'], [' '], ['zhōng', 'zhòng'], ['xīn']]

    pinyin('二个2个 中心', style=Style.FIRST_LETTER)  # 设置拼音风格
    # [['e'], ['g'], ['2'], ['g'], [' '], ['z'], ['x']]

    pinyin('二个2个 中心', style=Style.TONE2, heteronym=True)
    # [['e4r'], ['ge4', 'ge3', 'ga4n'], ['2'], ['ge4', 'ge3', 'ga4n'], [' '], ['zho1ng', 'zho4ng'], ['xi1n']]

    pinyin('二个2个 中心', style=Style.TONE3, heteronym=True)
    # [['er4'], ['ge4', 'ge3', 'gan4'], ['2'], ['ge4', 'ge3', 'gan4'], [' '], ['zhong1', 'zhong4'], ['xin1']]

    pinyin('二个2个 中心', style=Style.BOPOMOFO)  # 注音风格
    # [['ㄦˋ'], ['ㄍㄜˋ'], ['2'], ['ㄍㄜˋ'], [' '], ['ㄓㄨㄥ'], ['ㄒㄧㄣ']]

    lazy_pinyin('二个2个 威妥玛拼音', style=Style.WADEGILES)
    # ['erh', 'ko', '2', 'ko', ' ', 'wei', "t'o", 'ma', "p'in", 'yin']

    lazy_pinyin('二个2个 中心')  # 不考虑多音字的情况
    # ['er', 'ge', '2', 'ge', ' ', 'zhong', 'xin']

    lazy_pinyin('二个2个 战略', v_to_u=True)  # 不使用 v 表示 ü
    # ['er', 'ge', '2', 'ge', ' ', 'zhan', 'lüe']

    lazy_pinyin('二个2个 衣裳', style=Style.TONE3, neutral_tone_with_five=True)
    # ['er4', 'ge4', '2', 'ge4', ' ', 'yi1', 'shang5']

    lazy_pinyin('二个2个 你好', style=Style.TONE2, tone_sandhi=True)
    # ['e4r', 'ge4', '2', 'ge4', ' ', 'ni2', 'ha3o']
