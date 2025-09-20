#!/usr/bin/env python3
"""
Interactive Bible Analytics Script
Allows users to specify any chapter and verse combination and provides comprehensive statistics
focused only on those matching passages across the entire Bible.
"""

import json
import sys
from pathlib import Path
from collections import defaultdict, Counter
import re
from datetime import datetime


class InteractiveBibleAnalytics:
    """Class to handle interactive Bible data analysis and statistics."""
    
    def __init__(self, bible_data):
        """
        Initialize with Bible data.
        
        Args:
            bible_data (dict): Dictionary containing Bible verses
        """
        self.bible_data = bible_data
        self.target_chapter = None
        self.target_verse = None
        self.matching_passages = {}
        self.analytics = {}
        
    def get_user_input(self):
        """Get chapter and verse from user input."""
        print("🎯 Interactive Bible Verse Analytics")
        print("=" * 50)
        print("Enter the chapter and verse you want to analyze across all books.")
        print("Example: Chapter 9, Verse 23")
        print()
        
        while True:
            try:
                chapter = input("📖 Enter Chapter Number: ").strip()
                if not chapter.isdigit():
                    print("❌ Please enter a valid chapter number.")
                    continue
                
                verse = input(" Enter Verse Number: ").strip()
                if not verse.isdigit():
                    print("❌ Please enter a valid verse number.")
                    continue
                
                self.target_chapter = chapter
                self.target_verse = verse
                
                print(f"\n✅ Searching for Chapter {chapter}, Verse {verse} across all books...")
                return True
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                sys.exit(0)
            except Exception as e:
                print(f"❌ Error: {e}")
                continue
    
    def extract_matching_passages(self):
        """Extract all passages matching the specified chapter and verse."""
        print(f" Extracting Chapter {self.target_chapter}, Verse {self.target_verse} passages...")
        
        for reference, text in self.bible_data.items():
            if ':' in reference:
                book_chapter, verse = reference.split(':', 1)
                
                # Check if this matches the target verse
                if verse == self.target_verse:
                    parts = book_chapter.split()
                    if len(parts) >= 2:
                        book_name = ' '.join(parts[:-1])
                        chapter_num = parts[-1]
                        
                        # Check if this matches the target chapter
                        if chapter_num == self.target_chapter:
                            self.matching_passages[reference] = text
        
        print(f"✅ Found {len(self.matching_passages)} matching passages")
        return self.matching_passages
    
    def analyze_seven_patterns(self):
        """Analyze ALL patterns related to the number 7 algorithmically, excluding bracketed text."""
        print("🔢 Analyzing comprehensive number 7 patterns...")
        
        # Helper function to remove bracketed text
        def remove_bracketed_text(text):
            """Remove text within square brackets [...]"""
            return re.sub(r'\[.*?\]', '', text)
        
        seven_patterns = {
            'explicit_seven': [],
            'numbers_divisible_by_7': [],
            'character_count_seven': [],
            'word_count_seven': [],
            'position_seven': [],
            'seven_in_reference': [],
            'biblical_seven_terms': [],
            'mathematical_sevens': [],
            'ordinal_sevens': []
        }
        
        # Define patterns algorithmically
        seven_word_patterns = {
            'basic': [r'\bseven\b', r'\bseventh\b', r'\bseventy\b', r'\bseventeen\b'],
            'compounds': [r'\bseventy-seven\b', r'\bseven-fold\b', r'\bsevenfold\b'],
            'related': [r'\bweek\b', r'\bsabbath\b', r'\bheptad\b', r'\brest\b']
        }
        
        # Biblical seven terms (common in scripture)
        biblical_terms = [
            'seven days', 'seven years', 'seven times', 'seven lamps',
            'seven spirits', 'seven churches', 'seven seals', 'seven trumpets',
            'seven bowls', 'seven heads', 'seven horns', 'seven eyes',
            'seven stars', 'seven candlesticks', 'seven angels', 'seven thunders'
        ]
        
        # Ordinal numbers divisible by 7
        ordinals_div_7 = [
            'seventh', 'fourteenth', 'twenty-first', 'twenty-eighth',
            'thirty-fifth', 'forty-second', 'forty-ninth', 'fifty-sixth',
            'sixty-third', 'seventieth', 'seventy-seventh'
        ]
        
        for reference, original_text in self.matching_passages.items():
            # Remove bracketed text for analysis
            text = remove_bracketed_text(original_text)
            text_lower = text.lower()
            
            # 1. Check reference for numbers divisible by 7
            ref_numbers = re.findall(r'\d+', reference)
            for num_str in ref_numbers:
                num = int(num_str)
                if num % 7 == 0 and num > 0:
                    seven_patterns['seven_in_reference'].append({
                        'reference': reference,
                        'number': num,
                        'multiple': num // 7
                    })
            
            # 2. Find all numbers in text divisible by 7 (excluding bracketed text)
            text_numbers = re.findall(r'\b\d+\b', text)
            for num_str in text_numbers:
                num = int(num_str)
                if num % 7 == 0 and num > 0:
                    seven_patterns['numbers_divisible_by_7'].append({
                        'reference': reference,
                        'number': num,
                        'multiple': num // 7,
                        'context': self._get_context_around_number(text, num_str)
                    })
            
            # 3. Check for seven-related word patterns (excluding bracketed text)
            for category, patterns in seven_word_patterns.items():
                for pattern in patterns:
                    matches = re.findall(pattern, text_lower)
                    if matches:
                        seven_patterns['explicit_seven'].append({
                            'reference': reference,
                            'category': category,
                            'pattern': pattern.replace('\\b', ''),
                            'matches': matches,
                            'count': len(matches)
                        })
            
            # 4. Check for biblical seven terms (excluding bracketed text)
            for term in biblical_terms:
                if term in text_lower:
                    seven_patterns['biblical_seven_terms'].append({
                        'reference': reference,
                        'term': term,
                        'context': self._get_context_around_term(text, term)
                    })
            
            # 5. Check for ordinal numbers divisible by 7 (excluding bracketed text)
            for ordinal in ordinals_div_7:
                if ordinal in text_lower:
                    seven_patterns['ordinal_sevens'].append({
                        'reference': reference,
                        'ordinal': ordinal,
                        'context': self._get_context_around_term(text, ordinal)
                    })
            
            # 6. Character count analysis (excluding bracketed text)
            char_count = len(text)
            if char_count % 7 == 0:
                seven_patterns['character_count_seven'].append({
                    'reference': reference,
                    'char_count': char_count,
                    'multiple': char_count // 7
                })
            
            # 7. Word count analysis (excluding bracketed text)
            word_count = len(text.split())
            if word_count % 7 == 0:
                seven_patterns['word_count_seven'].append({
                    'reference': reference,
                    'word_count': word_count,
                    'multiple': word_count // 7
                })
        
        # 8. Position-based analysis (every 7th passage)
        passage_list = list(self.matching_passages.items())
        for i, (reference, text) in enumerate(passage_list, 1):
            if i % 7 == 0:
                seven_patterns['position_seven'].append({
                    'reference': reference,
                    'position': i,
                    'multiple': i // 7
                })
        
        # 9. Mathematical patterns across all passages (excluding bracketed text)
        cleaned_texts = [remove_bracketed_text(text) for text in self.matching_passages.values()]
        all_text = ' '.join(cleaned_texts)
        mathematical_sevens = []
        
        # Total character count (excluding bracketed text)
        total_chars = len(all_text)
        if total_chars % 7 == 0:
            mathematical_sevens.append({
                'type': 'combined_character_count',
                'value': total_chars,
                'multiple': total_chars // 7
            })
        
        # Total word count (excluding bracketed text)
        total_words = len(all_text.split())
        if total_words % 7 == 0:
            mathematical_sevens.append({
                'type': 'combined_word_count',
                'value': total_words,
                'multiple': total_words // 7
            })
        
        # Passage count
        if len(self.matching_passages) % 7 == 0:
            mathematical_sevens.append({
                'type': 'total_passage_count',
                'value': len(self.matching_passages),
                'multiple': len(self.matching_passages) // 7
            })
        
        seven_patterns['mathematical_sevens'] = mathematical_sevens
        
        # Calculate summary
        self.seven_patterns = {
            'patterns': seven_patterns,
            'summary': {
                'total_explicit_mentions': len(seven_patterns['explicit_seven']),
                'total_divisible_numbers': len(seven_patterns['numbers_divisible_by_7']),
                'total_biblical_terms': len(seven_patterns['biblical_seven_terms']),
                'total_ordinal_sevens': len(seven_patterns['ordinal_sevens']),
                'total_mathematical_patterns': len(mathematical_sevens),
                'passages_with_char_count_div_7': len(seven_patterns['character_count_seven']),
                'passages_with_word_count_div_7': len(seven_patterns['word_count_seven']),
                'position_based_sevens': len(seven_patterns['position_seven']),
                'references_with_seven': len(seven_patterns['seven_in_reference'])
            }
        }
        
        return self.seven_patterns
    
    def _get_context_around_number(self, text, number_str):
        """Get 60 characters of context around a number."""
        index = text.find(number_str)
        if index != -1:
            start = max(0, index - 30)
            end = min(len(text), index + len(number_str) + 30)
            return text[start:end].strip()
        return text[:60] + "..." if len(text) > 60 else text
    
    def _get_context_around_term(self, text, term):
        """Get 60 characters of context around a term."""
        index = text.lower().find(term.lower())
        if index != -1:
            start = max(0, index - 30)
            end = min(len(text), index + len(term) + 30)
            return text[start:end].strip()
        return text[:60] + "..." if len(text) > 60 else text

    def identify_all_books(self):
        """Identifies all unique book names present in the loaded Bible data."""
        print("📚 Identifying all unique books in the Bible...")
        self.all_books = set()
        for reference in self.bible_data.keys():
            if ':' in reference:
                book_chapter = reference.split(':')[0]
                book_name_parts = book_chapter.split()
                if len(book_name_parts) > 1 and book_name_parts[-1].isdigit():
                    book_name = ' '.join(book_name_parts[:-1])
                else:
                    book_name = book_chapter
                self.all_books.add(book_name)
        print(f"✅ Identified {len(self.all_books)} unique books.")

    def analyze_matching_passages(self):
        """Perform comprehensive analysis ONLY on the matching passages."""
        if not self.matching_passages:
            return {}
        
        print(f"📊 Analyzing {len(self.matching_passages)} matching passages...")

        # Identify books that contain the target passage
        self.books_with_target = set()
        for reference in self.matching_passages.keys():
            if ':' in reference:
                book_chapter = reference.split(':')[0]
                book_name_parts = book_chapter.split()
                if len(book_name_parts) > 1 and book_name_parts[-1].isdigit():
                    book_name = ' '.join(book_name_parts[:-1])
                else:
                    book_name = book_chapter
                self.books_with_target.add(book_name)

        # Identify books that do not contain the target passage
        self.books_without_target = self.all_books - self.books_with_target

        # Helper function to remove bracketed text
        def remove_bracketed_text(text):
            """Remove text within square brackets [...]"""
            return re.sub(r'\[.*?\]', '', text)

        # Basic text statistics (ONLY for matching passages, excluding bracketed text)
        cleaned_texts = [remove_bracketed_text(text) for text in self.matching_passages.values()]
        total_chars = sum(len(text) for text in cleaned_texts)
        total_words = sum(len(text.split()) for text in cleaned_texts)
        total_sentences = sum(len(re.split(r'[.!?]+', text)) for text in cleaned_texts)
        
        # Find extremes (ONLY for matching passages, excluding bracketed text)
        cleaned_passages = {ref: remove_bracketed_text(text) for ref, text in self.matching_passages.items()}
        longest_passage = max(cleaned_passages.items(), key=lambda x: len(x[1]))
        shortest_passage = min(cleaned_passages.items(), key=lambda x: len(x[1]))
        
        longest_by_words = max(cleaned_passages.items(), key=lambda x: len(x[1].split()))
        shortest_by_words = min(cleaned_passages.items(), key=lambda x: len(x[1].split()))
        
        # Word analysis (ONLY for matching passages, excluding bracketed text)
        all_words = []
        for text in cleaned_texts:
            words = re.findall(r'\b\w+\b', text.lower())
            all_words.extend(words)
        
        word_frequency = Counter(all_words)
        most_common_words = word_frequency.most_common(15)
        unique_words = len(set(all_words))
        
        # Character analysis (ONLY for matching passages, excluding bracketed text)
        all_chars = ''.join(cleaned_texts)
        char_frequency = Counter(all_chars.lower())
        most_common_chars = char_frequency.most_common(10)
        
        # Punctuation analysis (ONLY for matching passages, excluding bracketed text)
        punctuation_count = sum(len(re.findall(r'[^\w\s]', text)) for text in cleaned_texts)
        
        # Length distribution analysis (ONLY for matching passages, excluding bracketed text)
        passage_lengths = [len(text) for text in cleaned_texts]
        word_counts = [len(text.split()) for text in cleaned_texts]
        
        # Calculate percentiles
        passage_lengths.sort()
        word_counts.sort()
        
        def percentile(data, p):
            if not data:
                return 0
            k = (len(data) - 1) * p / 100
            f = int(k)
            c = k - f
            if f + 1 < len(data):
                return data[f] * (1 - c) + data[f + 1] * c
            return data[f]
        
        # Text complexity analysis (ONLY for matching passages, excluding bracketed text)
        avg_sentence_length = total_words / total_sentences if total_sentences > 0 else 0
        
        # Special character analysis (ONLY for matching passages, excluding bracketed text)
        special_chars = sum(len(re.findall(r'[^\w\s]', text)) for text in cleaned_texts)
        
        self.analytics = {
            'target_info': {
                'chapter': self.target_chapter,
                'verse': self.target_verse,
                'total_matching_passages': len(self.matching_passages)
            },
            'basic_stats': {
                'total_passages': len(self.matching_passages),
                'total_characters': total_chars,
                'total_words': total_words,
                'total_sentences': total_sentences,
                'unique_words': unique_words,
                'punctuation_count': punctuation_count,
                'special_chars': special_chars
            },
            'averages': {
                'avg_chars_per_passage': total_chars / len(self.matching_passages),
                'avg_words_per_passage': total_words / len(self.matching_passages),
                'avg_sentences_per_passage': total_sentences / len(self.matching_passages),
                'avg_sentence_length': avg_sentence_length,
                'avg_chars_per_word': total_chars / total_words if total_words > 0 else 0
            },
            'extremes': {
                'longest_passage': longest_passage,
                'shortest_passage': shortest_passage,
                'longest_by_words': longest_by_words,
                'shortest_by_words': shortest_by_words
            },
            'word_analysis': {
                'most_common_words': most_common_words,
                'word_frequency': word_frequency
            },
            'character_analysis': {
                'most_common_chars': most_common_chars,
                'char_frequency': char_frequency
            },
            'book_analysis': {
                'books_with_passage': list(self.books_with_target),
                'books_without_passage': list(self.books_without_target),
                'total_books_in_bible': len(self.all_books),
                'books_with_target_count': len(self.books_with_target),
                'books_without_target_count': len(self.books_without_target)
            },
            'length_distribution': {
                'passage_lengths': passage_lengths,
                'word_counts': word_counts,
                'percentiles': {
                    '25th_char': percentile(passage_lengths, 25),
                    '50th_char': percentile(passage_lengths, 50),
                    '75th_char': percentile(passage_lengths, 75),
                    '25th_word': percentile(word_counts, 25),
                    '50th_word': percentile(word_counts, 50),
                    '75th_word': percentile(word_counts, 75)
                }
            }
        }
        
        return self.analytics
    
    def display_seven_patterns(self):
        """Display comprehensive number 7 pattern analysis."""
        print("🔢 COMPREHENSIVE NUMBER 7 PATTERN ANALYSIS")
        print("-" * 50)
        
        patterns = self.seven_patterns['patterns']
        summary = self.seven_patterns['summary']
        
        # Summary statistics
        print("📊 SEVEN PATTERN SUMMARY:")
        print(f"  Explicit seven mentions: {summary['total_explicit_mentions']}")
        print(f"  Numbers divisible by 7: {summary['total_divisible_numbers']}")
        print(f"  Biblical seven terms: {summary['total_biblical_terms']}")
        print(f"  Ordinal sevens: {summary['total_ordinal_sevens']}")
        print(f"  Mathematical patterns: {summary['total_mathematical_patterns']}")
        print(f"  Passages with char count ÷ 7: {summary['passages_with_char_count_div_7']}")
        print(f"  Passages with word count ÷ 7: {summary['passages_with_word_count_div_7']}")
        print(f"  Position-based sevens: {summary['position_based_sevens']}")
        print(f"  References containing seven: {summary['references_with_seven']}")
        print()
        
        # Detailed pattern analysis
        if patterns['explicit_seven']:
            print("🔢 EXPLICIT SEVEN MENTIONS:")
            for item in patterns['explicit_seven']:
                print(f"  • {item['reference']} - {item['pattern']}: {item['count']} times")
            print()
        
        if patterns['numbers_divisible_by_7']:
            print("🔢 NUMBERS DIVISIBLE BY 7:")
            for item in patterns['numbers_divisible_by_7']:
                print(f"  • {item['reference']}: {item['number']} (7×{item['multiple']})")
                print(f"    Context: \"{item['context']}\"")
            print()
        
        if patterns['biblical_seven_terms']:
            print("🔢 BIBLICAL SEVEN TERMS:")
            for item in patterns['biblical_seven_terms']:
                print(f"  • {item['reference']}: '{item['term']}'")
                print(f"    Context: \"{item['context']}\"")
            print()
        
        if patterns['character_count_seven']:
            print("🔢 CHARACTER COUNTS DIVISIBLE BY 7:")
            for item in patterns['character_count_seven']:
                print(f"  • {item['reference']}: {item['char_count']} chars (7×{item['multiple']})")
            print()
        
        if patterns['word_count_seven']:
            print("🔢 WORD COUNTS DIVISIBLE BY 7:")
            for item in patterns['word_count_seven']:
                print(f"  • {item['reference']}: {item['word_count']} words (7×{item['multiple']})")
            print()
        
        if patterns['position_seven']:
            print("🔢 POSITION-BASED SEVENS (Every 7th passage):")
            for item in patterns['position_seven']:
                print(f"  • Position {item['position']}: {item['reference']} (7×{item['multiple']})")
            print()
        
        if patterns['seven_in_reference']:
            print("🔢 REFERENCES WITH NUMBERS DIVISIBLE BY 7:")
            for item in patterns['seven_in_reference']:
                print(f"  • {item['reference']}: {item['number']} (7×{item['multiple']})")
            print()
        
        if patterns['mathematical_sevens']:
            print("🔢 MATHEMATICAL SEVEN PATTERNS:")
            for item in patterns['mathematical_sevens']:
                print(f"  • {item['type']}: {item['value']} (7×{item['multiple']})")
            print()
        
        if patterns['ordinal_sevens']:
            print("🔢 ORDINAL NUMBERS RELATED TO SEVEN:")
            for item in patterns['ordinal_sevens']:
                print(f"  • {item['reference']}: '{item['ordinal']}'")
                print(f"    Context: \"{item['context']}\"")
            print()

    def display_comprehensive_analysis(self):
        """Display comprehensive analysis results."""
        if not self.matching_passages:
            print(f"❌ No passages found for Chapter {self.target_chapter}, Verse {self.target_verse}")
            return
        
        print("\n" + "="*80)
        print(f"📈 COMPREHENSIVE ANALYSIS: CHAPTER {self.target_chapter}, VERSE {self.target_verse}")
        print("="*80)
        print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Basic Statistics
        print("📊 BASIC STATISTICS")
        print("-" * 40)
        stats = self.analytics['basic_stats']
        print(f"Total Passages Found: {stats['total_passages']}")
        print(f"Total Characters: {stats['total_characters']:,}")
        print(f"Total Words: {stats['total_words']:,}")
        print(f"Total Sentences: {stats['total_sentences']:,}")
        print(f"Unique Words: {stats['unique_words']:,}")
        print(f"Punctuation Marks: {stats['punctuation_count']:,}")
        print(f"Special Characters: {stats['special_chars']:,}")
        print()
        
        # Averages
        print(" AVERAGE STATISTICS")
        print("-" * 40)
        avgs = self.analytics['averages']
        print(f"Average Characters per Passage: {avgs['avg_chars_per_passage']:.1f}")
        print(f"Average Words per Passage: {avgs['avg_words_per_passage']:.1f}")
        print(f"Average Sentences per Passage: {avgs['avg_sentences_per_passage']:.1f}")
        print(f"Average Sentence Length: {avgs['avg_sentence_length']:.1f} words")
        print(f"Average Characters per Word: {avgs['avg_chars_per_word']:.1f}")
        print()
        
        # Extremes
        print("🎯 EXTREME VALUES")
        print("-" * 40)
        extremes = self.analytics['extremes']
        print(f"Longest Passage (by chars): {extremes['longest_passage'][0]}")
        print(f"  Length: {len(extremes['longest_passage'][1])} characters")
        print(f"  Text: \"{extremes['longest_passage'][1][:100]}{'...' if len(extremes['longest_passage'][1]) > 100 else ''}\"")
        print()
        print(f"Shortest Passage (by chars): {extremes['shortest_passage'][0]}")
        print(f"  Length: {len(extremes['shortest_passage'][1])} characters")
        print(f"  Text: \"{extremes['shortest_passage'][1]}\"")
        print()
        print(f"Longest Passage (by words): {extremes['longest_by_words'][0]}")
        print(f"  Words: {len(extremes['longest_by_words'][1].split())}")
        print()
        print(f"Shortest Passage (by words): {extremes['shortest_by_words'][0]}")
        print(f"  Words: {len(extremes['shortest_by_words'][1].split())}")
        print()
        
        # Length Distribution
        print("📏 LENGTH DISTRIBUTION")
        print("-" * 40)
        dist = self.analytics['length_distribution']
        print(f"Character Length Percentiles:")
        print(f"  25th: {dist['percentiles']['25th_char']:.0f} chars")
        print(f"  50th: {dist['percentiles']['50th_char']:.0f} chars")
        print(f"  75th: {dist['percentiles']['75th_char']:.0f} chars")
        print()
        print(f"Word Count Percentiles:")
        print(f"  25th: {dist['percentiles']['25th_word']:.0f} words")
        print(f"  50th: {dist['percentiles']['50th_word']:.0f} words")
        print(f"  75th: {dist['percentiles']['75th_word']:.0f} words")
        print()
        
        # Book Analysis
        print("📚 BOOK ANALYSIS")
        print("-" * 40)
        book_analysis = self.analytics['book_analysis']
        print(f"Books containing Chapter {self.target_chapter}, Verse {self.target_verse}: {book_analysis['books_with_target_count']}")
        print()
        for book in book_analysis['books_with_passage']:
            print(f"  {book}")
        print()
        
        # Word Analysis
        print("🔤 WORD ANALYSIS")
        print("-" * 40)
        word_analysis = self.analytics['word_analysis']
        print("Most Common Words:")
        for i, (word, count) in enumerate(word_analysis['most_common_words'][:10], 1):
            print(f"  {i:2d}. '{word}': {count} times")
        print()
        
        # Character Analysis
        print("🔢 CHARACTER ANALYSIS")
        print("-" * 40)
        char_analysis = self.analytics['character_analysis']
        print("Most Common Characters:")
        
        # Filter out spaces and show only non-space characters
        non_space_chars = [(char, count) for char, count in char_analysis['most_common_chars'] if char != ' ']
        for i, (char, count) in enumerate(non_space_chars[:7], 1):
            print(f"  {i:2d}. '{char}': {count} times")
        print()
        
        # Number 7 Pattern Analysis
        self.display_seven_patterns()
        
        # All Matching Passages
        print("📖 ALL MATCHING PASSAGES")
        print("-" * 40)
        for i, (reference, text) in enumerate(self.matching_passages.items(), 1):
            print(f"{i:2d}. {reference}")
            print(f"    Length: {len(text)} chars, {len(text.split())} words")
            print(f"    Text: \"{text}\"")
            print()
    
    def save_analysis_report(self, output_dir="./"):
        """Save detailed analysis report to files."""
        if not self.matching_passages:
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save matching passages
        passages_file = f"{output_dir}chapter_{self.target_chapter}_verse_{self.target_verse}_passages_{timestamp}.json"
        with open(passages_file, 'w', encoding='utf-8') as f:
            json.dump(self.matching_passages, f, indent=2, ensure_ascii=False)
        print(f" Passages saved to: {passages_file}")
        
        # Save comprehensive analytics
        analytics_file = f"{output_dir}chapter_{self.target_chapter}_verse_{self.target_verse}_analytics_{timestamp}.json"
        report_data = {
            'search_parameters': {
                'chapter': self.target_chapter,
                'verse': self.target_verse,
                'timestamp': datetime.now().isoformat()
            },
            'passages': self.matching_passages,
            'analytics': self.analytics
        }
        
        with open(analytics_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        print(f"💾 Analytics report saved to: {analytics_file}")
        
        # Save summary report
        summary_file = f"{output_dir}chapter_{self.target_chapter}_verse_{self.target_verse}_summary_{timestamp}.txt"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(f"BIBLE ANALYTICS SUMMARY\n")
            f.write(f"Chapter {self.target_chapter}, Verse {self.target_verse}\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*50 + "\n\n")
            
            f.write(f"Total Passages Found: {self.analytics['basic_stats']['total_passages']}\n")
            f.write(f"Total Characters: {self.analytics['basic_stats']['total_characters']:,}\n")
            f.write(f"Total Words: {self.analytics['basic_stats']['total_words']:,}\n")
            f.write(f"Average Length: {self.analytics['averages']['avg_chars_per_passage']:.1f} characters\n")
            f.write(f"Average Words: {self.analytics['averages']['avg_words_per_passage']:.1f}\n\n")
            
            f.write("PASSAGES:\n")
            f.write("-"*20 + "\n")
            for reference, text in self.matching_passages.items():
                f.write(f"{reference}: {text}\n")
        
        print(f"💾 Summary report saved to: {summary_file}")


def load_bible_data(bible_json_path):
    """Load Bible data from JSON file."""
    try:
        print(f" Loading Bible data from: {bible_json_path}")
        with open(bible_json_path, 'r', encoding='utf-8') as file:
            bible_data = json.load(file)
        print(f"✅ Successfully loaded {len(bible_data):,} verses")
        return bible_data
    except FileNotFoundError:
        print(f"❌ Error: File '{bible_json_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format: {e}")
        return None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None


def main():
    """Main function to execute the interactive analytics script."""
    print("🚀 Interactive Bible Verse Analytics")
    print("=" * 50)
    
    # Default path to the Bible JSON file
    default_bible_path = "/home/cyak/Downloads/bible.json"
    
    # Check if a custom path was provided as command line argument
    if len(sys.argv) > 1:
        bible_json_path = sys.argv[1]
    else:
        bible_json_path = default_bible_path
    
    # Verify the file exists
    if not Path(bible_json_path).exists():
        print(f"❌ Error: Bible JSON file not found at '{bible_json_path}'")
        print("Usage: python countverse.py [path_to_bible.json]")
        sys.exit(1)
    
    # Load Bible data
    bible_data = load_bible_data(bible_json_path)
    if not bible_data:
        sys.exit(1)
    
    # Initialize analytics
    analytics = InteractiveBibleAnalytics(bible_data)
    
    # Get user input
    if not analytics.get_user_input():
        sys.exit(1)
    
    # Perform analysis
    analytics.identify_all_books()
    analytics.extract_matching_passages()
    analytics.analyze_matching_passages()
    analytics.analyze_seven_patterns()
    
    # Display results
    analytics.display_comprehensive_analysis()
    
    # Save reports
    analytics.save_analysis_report()
    
    print("\n🎉 Analysis complete!")
    print(f" Analyzed Chapter {analytics.target_chapter}, Verse {analytics.target_verse}")
    print(f"📈 Found {len(analytics.matching_passages)} matching passages")


if __name__ == "__main__":
    main()
