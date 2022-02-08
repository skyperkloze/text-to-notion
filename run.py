from bot import Bot
def main():
    updater.dispatcher.logger.addFilter((lambda s: not s.msg.endswith('A TelegramError was raised while processing the Update')))
    bot = Bot()
    bot.run() 
    
    

if __name__ == '__main__':
    main()
