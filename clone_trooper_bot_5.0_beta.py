# -*- coding: utf-8 -*-
"""
Created on Mon April 25 22:44:00 2021

@author: MAD_MAL1CE
"""

import praw
import random
import time

print(praw.__path__)
                
#The time in seconds between posts
cooldown = 5
 
# Put your bot's reddit id here. It will be used in several funtions.
bot_id = "dzuogrxz"
battle_droid_id = "hq2b7ayx"

# Put your bot's reddit id here. It will be used in several funtions.
bot_id = "dzuogrxz"

# Connecting your bot to your personal script app and logging in
reddit = praw.Reddit('CloneTrooper')
print("Logged In Successfully!")

# Begins the comment stream, scans for new comments

def Get_Triggers():
    
    clone_list_txt = open('clone_names/A1_clones_list.txt', 'r')
    clone_list = clone_list_txt.read().splitlines()
    clone_list_txt.close()
    
    clone_triggers_txt = open('triggers/clone_triggers.txt', 'r')
    clone_triggers = clone_triggers_txt.read().splitlines()
    clone_triggers_txt.close()
    
    follow_orders_triggers = ["good soldiers follow orders"]
    
    prisoners_triggers = ["do we take prisoners"]
    
    the_creeps_triggers_txt = open('triggers/the_creeps_triggers.txt', 'r')
    the_creeps_triggers = the_creeps_triggers_txt.read().splitlines()
    the_creeps_triggers_txt.close()
    
    good_bot_triggers_txt = open('triggers/good_bot_triggers.txt', 'r')
    good_bot_triggers = good_bot_triggers_txt.read().splitlines()
    good_bot_triggers_txt.close()
    
    bomb_triggers_txt = open('triggers/bomb_triggers.txt', 'r')
    bomb_triggers = bomb_triggers_txt.read().splitlines()
    bomb_triggers_txt.close()
    
    bad_bot_triggers_txt = open('triggers/bad_bot_triggers.txt', 'r')
    bad_bot_triggers = bad_bot_triggers_txt.read().splitlines()
    bad_bot_triggers_txt.close()
    
    skirata_triggers = ["skirata"]
    
    sentient_triggers_txt = open('triggers/sentient_triggers.txt', 'r')
    sentient_triggers = sentient_triggers_txt.read().splitlines()
    sentient_triggers_txt.close()
    
    order_66_triggers_txt = open('triggers/order_66_triggers.txt', 'r')
    order_66_triggers = order_66_triggers_txt.read().splitlines()
    order_66_triggers_txt.close()
    
    order_67_triggers = ["order 67"]
    
    order_69_triggers_txt = open('triggers/order_69_triggers.txt', 'r')
    order_69_triggers = order_69_triggers_txt.read().splitlines()
    order_69_triggers_txt.close()
    
    stormtrooper_filter_txt = open('triggers/bark_triggers.txt', 'r')
    stormtrooper_filter = stormtrooper_filter_txt.read().splitlines()
    stormtrooper_filter_txt.close()
    
    bark_triggers_txt = open('triggers/bark_triggers.txt', 'r')
    bark_triggers = bark_triggers_txt.read().splitlines()
    bark_triggers_txt.close()
    
    expendable_triggers_txt = open('triggers/expendable_triggers.txt', 'r')
    expendable_triggers = expendable_triggers_txt.read().splitlines()
    expendable_triggers_txt.close()
    
    expendable_triggers_txt = open('triggers/expendable_triggers.txt', 'r')
    expendable_triggers = expendable_triggers_txt.read().splitlines()
    expendable_triggers_txt.close()
    
    lightsaber_triggers = ["lightsaber",
                           "light saber",
                           "lasersword",
                           "laser sword"]
    
    why_triggers = ["why",
                    "explain",
                    "i dont understand"]
    
    war_triggers = [" war",
                    "war ",
                    "wars ",
                    " wars"]
    
    programmed_triggers = ["programmed",
                            "programming",
                            "thinking",
                            "intelligent",
                            "smart"]
    
    kill_count_triggers = ["how many kills",
                           "kill count"]
    
    trandoshan_triggers = ["trandoshan",
                           "lizard"]
    
    geonosis_triggers = ["geonosis",
                         "geonosians",
                         "bugs",
                         " bug",
                         "bug "]
    
    redredgreen_triggers = ["red red green",
                            "red green red"]
    
    egg_triggers = [" egg",
                    "egg ",
                    " eggs",
                    "eggs "]
    
    return clone_list, clone_triggers, follow_orders_triggers, prisoners_triggers, the_creeps_triggers, expendable_triggers, lightsaber_triggers, why_triggers, war_triggers, programmed_triggers, kill_count_triggers, trandoshan_triggers, geonosis_triggers, redredgreen_triggers, egg_triggers, good_bot_triggers, bomb_triggers, bad_bot_triggers, skirata_triggers, sentient_triggers, order_66_triggers, order_67_triggers, order_69_triggers, stormtrooper_filter, bark_triggers

def Add_To_Ignore_List():
    with open('lists/ignore_list.txt', 'a') as f: # Opens ignore list in append mode
                                
        print(author_name)
        print(author_id)
        print("cake day: ", cake_day)
        print(comment_lower)
        print("\n\n")
        
        # Writes Username and ID of user to the ignore list
        f.write(author_name + "\n")
        f.write(author_id+ "\n")
        print("!!!!! User Added to Ignore List !!!!!")

        # Replies to user comment
        with open('responses/farewell_responses.txt', 'r', encoding='utf-8') as tf:
                                     
                quote_selection = tf.read().splitlines()
            
                print("===== Generating Reply =====", "\n")
                generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
                generated_reply = generated_reply_unadjusted.replace("username", author_name)
                comment.reply(generated_reply) # Replies to comment with random quote
                print(generated_reply, "\n") # Prints random quote from reply
                print("===== Reply Posted ======", "\n\n")
                
                return

def Quote_Selection(quote_list_txt):
    
    if clone_saved == True:
                                        
        with open(quote_list_txt, 'r', encoding='utf-8') as tf:
        
            print("===== Generating Reply =====", "\n")
            possible_responses = tf.read().splitlines()
            narrowed_responses = [q for q in possible_responses if this_clone_random_str in q]
            if narrowed_responses == []:
                print("List Empty, Reverting to Default List")
                with open('responses/clone_responses.txt', 'r', encoding='utf-8') as tf:
                    possible_responses = tf.read().splitlines()
                    narrowed_responses = [q for q in possible_responses if this_clone_random_str in q]
            
            generated_reply_unadjusted = random.choice(narrowed_responses) # Fetch random quote from list
            generated_reply = generated_reply_unadjusted.replace("username", author_name)
            if generated_reply == comment.parent().body:
                print("!!!!! Duplicate Detected, Retrying !!!!!")
                narrowed_responses = [q for q in possible_responses if this_clone_random_str in q]
                generated_reply_unadjusted = random.choice(narrowed_responses) # Fetch random quote from list
                generated_reply = generated_reply_unadjusted.replace("username", author_name)
                if generated_reply == comment.parent().body:
                    print("!!!!! Duplicate Detected, Retrying !!!!!")
                    with open('responses/clone_responses.txt', 'r', encoding='utf-8') as tf:
                        possible_responses = tf.read().splitlines()
                        narrowed_responses = [q for q in possible_responses if this_clone_random_str in q]
                        generated_reply_unadjusted = random.choice(narrowed_responses) # Fetch random quote from list
                        generated_reply = generated_reply_unadjusted.replace("username", author_name)
                
            if generated_reply != comment.parent().body:
                comment.reply(generated_reply) # Replies to comment with random quote
                print(generated_reply, "\n") # Prints random quote from reply
                print("===== Reply Posted ======", "\n\n\n")
                time.sleep(cooldown) # Cooldown in seconds
            else:
                print("!!!!! Too Many Retries, Terminating Reply !!!!!")
            
    else:
    
        with open(quote_list_txt, 'r', encoding='utf-8') as tf:
            
            quote_selection = tf.read().splitlines()
            print("===== Generating Reply =====", "\n")
            generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
            generated_reply = generated_reply_unadjusted.replace("username", author_name)
            comment.reply(generated_reply) # Replies to comment with random quote
            print(generated_reply, "\n") # Prints random quote from reply
            print("===== Reply Posted ======", "\n")
            time.sleep(cooldown) # Cooldown in seconds
            
def Quote_Selection_Keyword_Priority(quote_list_txt):
    
    if clone_saved == True:
                                        
        with open(quote_list_txt, 'r', encoding='utf-8') as tf:
        
            print("===== Generating Reply =====", "\n")
            possible_responses = tf.read().splitlines()
            narrowed_responses = [q for q in possible_responses if this_clone_random_str in q]
            if narrowed_responses == []:
                print("List Empty, Removing Saved Clone")
                possible_responses = tf.read().splitlines()
                narrowed_responses = possible_responses
            
            generated_reply_unadjusted = random.choice(narrowed_responses) # Fetch random quote from list
            generated_reply = generated_reply_unadjusted.replace("username", author_name)
            if generated_reply == comment.parent().body:
                print("!!!!! Duplicate Detected, Retrying !!!!!")
                narrowed_responses = [q for q in possible_responses if this_clone_random_str in q]
                generated_reply_unadjusted = random.choice(narrowed_responses) # Fetch random quote from list
                generated_reply = generated_reply_unadjusted.replace("username", author_name)
                if generated_reply == comment.parent().body:
                    print("!!!!! Duplicate Detected, Retrying !!!!!")
                    with open('responses/clone_responses.txt', 'r', encoding='utf-8') as tf:
                        possible_responses = tf.read().splitlines()
                        narrowed_responses = [q for q in possible_responses if this_clone_random_str in q]
                        generated_reply_unadjusted = random.choice(narrowed_responses) # Fetch random quote from list
                        generated_reply = generated_reply_unadjusted.replace("username", author_name)
                
            if generated_reply != comment.parent().body:
                comment.reply(generated_reply) # Replies to comment with random quote
                print(generated_reply, "\n") # Prints random quote from reply
                print("===== Reply Posted ======", "\n\n\n")
                time.sleep(cooldown) # Cooldown in seconds
            else:
                print("!!!!! Too Many Retries, Terminating Reply !!!!!")
            
    else:
    
        with open(quote_list_txt, 'r', encoding='utf-8') as tf:
            
            quote_selection = tf.read().splitlines()
            print("===== Generating Reply =====", "\n")
            generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
            generated_reply = generated_reply_unadjusted.replace("username", author_name)
            comment.reply(generated_reply) # Replies to comment with random quote
            print(generated_reply, "\n") # Prints random quote from reply
            print("===== Reply Posted ======", "\n")
            time.sleep(cooldown) # Cooldown in seconds

#BEGINNING OF WHILE LOOP!
while True:

    try:
        clone_list, clone_triggers, follow_orders_triggers, prisoners_triggers, the_creeps_triggers, expendable_triggers, lightsaber_triggers, why_triggers, war_triggers, programmed_triggers, kill_count_triggers, trandoshan_triggers, geonosis_triggers, redredgreen_triggers, egg_triggers, good_bot_triggers, bomb_triggers, bad_bot_triggers, skirata_triggers, sentient_triggers, order_66_triggers, order_67_triggers, order_69_triggers, stormtrooper_filter, bark_triggers = Get_Triggers()
        print("Retrieved Triggers!!!")
        
        for comment in reddit.subreddit('PrequelMemes+botmakers_guild').stream.comments(skip_existing=True):
            
            author_name = str(comment.author.name) # Fetch author name
            author_id = str(comment.author.id) # Fetch author id
            comment_id = str(comment.id)
            comment_lower = comment.body.lower() # Fetch comment body and convert to lowercase
            redditor = reddit.redditor(author_name)
            cake_day = time.strftime("%D", time.gmtime(redditor.created_utc))
            cake_day_str = cake_day[0:5]
            todays_date = time.strftime("%D", time.gmtime(comment.created_utc))
            todays_date_str = todays_date[0:5]
            cake_day_characters = 'oaschjr159_'
            is_cake_day = False
            
            with open('lists/cake_day_list.txt', 'r')as cd:
                cd_contents = cd.read()
                if author_id not in cd and cake_day_str == todays_date_str and cake_day != todays_date and author_id[0] in cake_day_characters:
                    is_cake_day = True
            
            clone_detected = False
            clone_saved = False
            if any(word in comment_lower for word in clone_list): #Looks for individual clones
                print('!!!!! Clone Detected !!!!!\n')
                this_clone = [word for word in clone_list if word in comment_lower]
                this_clone_str = str(this_clone)
                this_clone_clipped = this_clone_str.replace('[', '').replace(']', '').replace('"', '').replace("'", '').strip()
                print("Clones Detected: " + this_clone_clipped)
                this_clone_clipped_list = this_clone_clipped.split(", ")
                this_clone_random = str(random.choice(this_clone_clipped_list))
                this_clone_random_str = this_clone_random.replace('[', '').replace(']', '').replace('"', '').replace("'", '').capitalize()
                print("Selected Clone: " + this_clone_random_str)
                clone_detected = True
            
            print("\n\n\n", "##### NEW COMMENT #####", "\n", "Submission Title: ", comment.submission.title)
            print("Clone Detected: ", clone_detected)
            
            if clone_detected == True:
                clone_saved = True
                with open('lists/saved_comment_list.txt', 'a') as scl:
                    
                    scl.write(comment_id)
                    scl.write("::")
                    scl.write(this_clone_random_str)
                    scl.write("::")
                    scl.write(author_id)
                    scl.write("::")
                    scl.write(todays_date)
                    scl.write("\n")
                    print('%%%%% Comment Saved %%%%%')
            
            with open('lists/saved_comment_list.txt', 'r') as scl:
            
                saved_comments_list = scl.read().split("\n")
                saved_comment = [item for item in saved_comments_list if comment.parent().id in item]
                if saved_comment != []:
                    
                    saved_comment_str = str(saved_comment).replace('[', '').replace(']', '').replace('"', '').replace("'", '')
                    print("Comment Parent ID: " + comment.parent().id)
                    saved_comment_parsed = saved_comment_str.split("::")
                    saved_id = saved_comment_parsed[0]
                    saved_clone = saved_comment_parsed[1]
                    saved_author = saved_comment_parsed[2]
                    saved_date = saved_comment_parsed[3]
                    print("Saved ID: " + saved_id)
                    print("Saved Clone: " + saved_clone)
                    print("Saved Author: " + saved_author)
                    print("Saved Date: " + saved_date)
                    clone_saved = True
                
            if clone_detected == False and saved_comment != []:
                this_clone_random_str = saved_clone
                clone_saved = True
                print('Saved Clone Detected: ' + saved_clone)

            with open('lists/ignore_list.txt', 'r')as rf: # Opens ignore_list in read only mode
                rf_contents = rf.read() # Reads the contents of ignore list
                if author_id not in rf_contents and author_id != bot_id: #Checks comment against ignore list and bot id
                    
                    with open('lists/gray_list.txt', 'r')as gl:
                        
                        gray_list = gl.read() # Reads the contents of ignore list
                        
                        if author_name in gray_list:
                            
                            is_graylisted = True
                            
                        else:
                            
                            is_graylisted = False
                        
                    if "!ignore" in comment_lower and len(comment_lower) < 10: # Looks for the word "ignore" in the comment and checks length of comment to prevent misfire.
                        
                        print("Checking for bot_id")
                        
                        if comment.parent().author.id == bot_id: # Checks if comment is a reply to your bot
                
                            Add_To_Ignore_List()
                                
                        else: # if ignore is not in response to your bot, prints a false alarm message and does not add name to ignore list
                            
                            print("##### NEW COMMENT #####")
                            print(author_name)
                            print(author_id)
                            print("cake day: ", cake_day)
                            print(comment_lower)
                            print("\n\n")
                            
                            print("\n")
                            print("&&&& False Alarm &&&&")
                            print("\n")
                            
                        
                    else: # If 'ignore' not present in comment body, prceeds to checking for keywords and other bot functions
                    
                        print("Author: ", comment.author)
                        print("Is Graylisted: ", is_graylisted)
                        print("Author ID: ", comment.author.id, "\n")
                        print("Today's Date: ", todays_date_str)
                        print(comment.body.lower(), "\n\n")
                        
                        
                        if is_graylisted == True:
                        
                            roll_die = random.randint(1, 30)
                            print("Dice Roll: ", roll_die)
                            roll_die_string = str(roll_die)
                            if roll_die_string == "1":
                                
                                is_graylisted = False
                                
                        if is_graylisted == False: #Begin Trigger Search and Quote Selection
                            
                            if is_cake_day == True: #Checks for keywords in comment
                                Quote_Selection_Keyword_Priority('responses/cake_day_responses.txt')
                            
                            elif any(word in comment_lower for word in sentient_triggers) and comment.parent().author.id == bot_id: 
                                    Quote_Selection_Keyword_Priority('responses/sentient_responses.txt')
                                    
                            elif any(word in comment_lower for word in egg_triggers):
                                
                                print("===== Generating Reply =====", "\n")
                                comment.reply('"Uh, what do ya know? They *are* eggs." -Scorch, Delta 62')
                                print('"Uh, what do ya know? They *are* eggs." -Scorch, Delta 62', "\n")
                                print("===== Reply Posted ======", "\n")
                                time.sleep(cooldown) # Cooldown in seconds
                                
                            elif any(word in comment_lower for word in bomb_triggers) and 'demolitions expert' not in comment_lower:
                                
                                print("===== Generating Reply =====", "\n")
                                comment.reply('"Was it red red green, or red green red?" -Scorch, Delta 62')
                                print('"Was it red red green, or red green red?" -Scorch, Delta 62', "\n")
                                print("===== Reply Posted ======", "\n")
                                time.sleep(cooldown) # Cooldown in seconds
                                
                            elif any(word in comment_lower for word in redredgreen_triggers):
                                
                                print("===== Generating Reply =====", "\n")
                                comment.reply('''"And he's supposed to be the demolitions expert." -Sev, Delta 07''') 
                                print('''"And he's supposed to be the demolitions expert." -Sev, Delta 07''', "\n")
                                print("===== Reply Posted ======", "\n")
                                time.sleep(cooldown) # Cooldown in seconds
                                
                            # elif any(word in comment_lower for word in can_the_chatter_triggers):
                                
                            #     print("===== Generating Reply =====", "\n")
                            #     comment.reply('') # Replies to comment with random quote
                            #     print('', "\n") # Prints random quote from reply
                            #     print("===== Reply Posted ======", "\n")
                            #     time.sleep(cooldown) # Cooldown in seconds
                            
                            elif any(word in comment_lower for word in skirata_triggers):
                                Quote_Selection_Keyword_Priority('responses/skirata_responses.txt')
                                
                            elif any(word in comment_lower for word in good_bot_triggers) and comment.parent().author.id == bot_id: #Checks for keywords in comment
                                    Quote_Selection_Keyword_Priority('responses/good_bot_responses.txt')
                                    
                            elif any(word in comment_lower for word in bad_bot_triggers) and comment.parent().author.id == bot_id: #Checks for keywords in comment
                                    Quote_Selection_Keyword_Priority('responses/bad_bot_responses.txt')
                                    
                            elif any(word in comment_lower for word in the_creeps_triggers):
                                Quote_Selection_Keyword_Priority('responses/the_creeps_responses.txt')
                                
                            elif any(word in comment_lower for word in follow_orders_triggers):
                                Quote_Selection('responses/follow_orders_responses.txt')
                                
                            elif any(word in comment_lower for word in order_67_triggers) and comment.parent().author.id == bot_id: #Checks for keywords in comment
                                    Quote_Selection_Keyword_Priority('responses/order_67_responses.txt')
                                    
                            elif any(word in comment_lower for word in order_69_triggers) and comment.parent().author.id == bot_id: #Checks for keywords in comment
                                    Quote_Selection_Keyword_Priority('responses/order_69_responses.txt')
                                    
                            elif any(word in comment_lower for word in order_66_triggers): #Checks for keywords in comment
                                    Quote_Selection_Keyword_Priority('responses/order_66_responses.txt')
                                    
                            elif any(word in comment_lower for word in bark_triggers):
                                Quote_Selection_Keyword_Priority('responses/BF2_barks.txt')
                                
                            elif any(word in comment_lower for word in kill_count_triggers) and comment.parent().author.id == bot_id:
                                    Quote_Selection_Keyword_Priority('responses/kill_count_responses.txt')
                                    
                            elif author_id == 'ly2ymnp3': #Gonk Bot ID
                                Quote_Selection_Keyword_Priority('responses/gonk_responses.txt')
                                
                            elif "grond" in comment_lower:
                                roll_die = random.randint(1, 2)
                                print("Dice Roll: ", roll_die)
                                roll_die_string = str(roll_die)
                                if roll_die_string == "1":
                                    Quote_Selection_Keyword_Priority('responses/grond_responses.txt')
                                
                            elif comment.author.id == battle_droid_id: # Checks if comment is a reply to your bot
                                Quote_Selection_Keyword_Priority('responses/droid_responses.txt')
                                    
                            elif (any(word in comment_lower for word in clone_triggers) and not any(word in comment_lower for word in stormtrooper_filter)) or (comment.parent().author.id == bot_id):
                                if any(word in comment_lower for word in expendable_triggers):
                                    Quote_Selection('responses/expendable_responses.txt')
                                    
                                elif any(word in comment_lower for word in why_triggers):
                                    Quote_Selection('responses/why_responses.txt')
                                    
                                elif any(word in comment_lower for word in war_triggers):
                                    Quote_Selection('responses/war_responses.txt')
                                
                                elif any(word in comment_lower for word in lightsaber_triggers):
                                    Quote_Selection('responses/lightsaber_responses.txt')
                                    
                                elif any(word in comment_lower for word in kill_count_triggers):
                                    Quote_Selection_Keyword_Priority('responses/kill_count_responses.txt')
                                    
                                elif any(word in comment_lower for word in programmed_triggers):
                                    Quote_Selection_Keyword_Priority('responses/programmed_responses.txt')
                                    
                                elif any(word in comment_lower for word in geonosis_triggers):
                                    Quote_Selection_Keyword_Priority('responses/geonosis_responses.txt')
                                    
                                elif '?' in comment_lower:
                                    Quote_Selection('responses/question_responses.txt')
                                    
                                else:
                                    Quote_Selection('responses/clone_responses.txt')
                                    
                            elif '?' in comment_lower and comment.parent().author.id == bot_id:
                                Quote_Selection('responses/question_responses.txt')
                                    
                        else:
                            
                            print("\n", "Roll failed, ignoring comment")
                            print("!!!!!!!! User Graylisted !!!!!!!!", "\n\n")
                                
                else: # If user on ignore list, prints User Ignored, and does not reply to comment
                    
                    print("\n", "##### NEW COMMENT #####", "\n")
                    print(comment.author)
                    print(comment.author.id)    
                    print(comment.body.lower(), "\n")
                    print("!!!!!!!! User Ignored !!!!!!!!", "\n\n")
        
    except Exception as e:
        print("Except happened: ", e)
        pass